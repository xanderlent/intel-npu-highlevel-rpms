# High-Level Software that uses the Intel AI Boost NPU

The goal of this repository is to provide Fedora packages for software that runs on the Intel NPU at a higher level than the driver.

You can find binary packages built from this repository in [my xanderlent/intel-npu-highlevel Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-highlevel/).

## Installation Instructions

- Enable the copr.
- Install the `python3-intel-npu-acceleration-library` package.
- Read [Intel's docs](https://intel.github.io/intel-npu-acceleration-library/) to get examples and learn how to use the package to run LLMs and other workloads on your NPU.

## More about the packages

Hopefully, with effort and care, these packages will eventually find their way upstream, into Fedora proper. (For now, the Fedora Review step has been disabled in copr because it drastically improves build times on small packages like these.) As of late January 2025, I am working within the Fedora AI/ML SIG to help get this code upstream.

Including the driver repo means I cannot easily provide aarch64 builds (without splitting the oneapi-level-zero dependency out into another copr). For now I am returning to only building on x86\_64, but I may consider that option in the future.

Right now, most of these packages are originally for Python, so they were generated with the [`pyp2spec`](https://github.com/befeleme/pyp2spec) tool. I'm not completely sure how to use it, so I might be missing some steps, but it definitely does not seem as automated as I would like in terms of converting Python packages to RPMs... On the other hand, [rust2rpm](https://pagure.io/fedora-rust/rust2rpm) was a breeze to use. (`rust2rpm --no-rpmautospec -t fedora --compat crate@version`, leave out `--compat` for non-versioned packages.)

## A note on system requirements

If you want to use this software with the Intel NPU, you will need to install the [driver](https://github.com/intel/linux-npu-driver) and have suitable hardware present in your system, which at present is an "Intel Core Ultra"-branded product from Intel's Meteor Lake, Lunar Lake, or Arrow Lake product lines.

I also unofficially maintain the driver packaging in [another project](https://github.com/xanderlent/intel-npu-driver-rpm), with binaries available in [my xanderlent/intel-npu-driver Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-driver/). Follow the directions there.

## List of software packaged

- [Intel NPU Acceleration Library](https://github.com/intel/intel-npu-acceleration-library)
	- A Python library for running various AI/ML workloads on the Intel NPU. They also provide some [docs](https://intel.github.io/intel-npu-acceleration-library/index.html).

## Support Status

My primary goal is supporting the above list of software packaged. All the deps have best-effort support for now, so that I can focus on making the NPU-related packages work.

- Fedora 39 and below are not supported, were never supported in the past, and likely will never be supported in the future.
- Fedora 40 is no longer supported, as it reached EOL in May 2025.
- Fedora 41 is supported. (OpenVINO is built as a backport from Fedora 42. Some deps are backported from rawhide.)
- Fedora 42 is supported. (Some deps are backported from rawhide.)
- Fedora rawhide is partially suppported, because sometimes it breaks and I can't immediately fix it.

### Packaged software and dependencies:
- python-intel-npu-acceleration-library (docs are not packaged due to additional deps)
  - openvino (only for F41, see below, packaged upstream in F42+)
  - python-neural-compressor (+pt)
    - python-accelerate
    - (opencv-python-headless was substituted with packaged opencv)
    - python-pycocotools
    - python-transformers (see below)
  - python-transformers (+accelerate,+ftfy,+num2words,+optuna,+sentencepiece,+serving,+sklearn,+tiktoken,+tokenizers,+torch,+torch-vision,+torchhub,+vision; future work for +onnx{,runtime},+modelcreation)
    - python-accelerate (see above)
    - python-blobfile
    - python-tokenizers
      - rust-numpy0.23
      - rust-tokenizers
        - rust-esaxx-rs
        - rust-macro\_rules\_attribute (backported from rawhide)
          - rust-macro\_rules\_attribute-proc\_macro (backported from rawhide)
        - rust-monostate (backported from rawhide)
          - rust-monostate-impl (backported from rawhide)
        - rust-rayon-cond (backported from rawhide)
        - rust-spm\_precompiled (backported from rawhide)
        - rust-unicode-normalization-alignments (backported from rawhide)
    - python-safetensors (backported from rawhide)
- python-datasets
- python-evaluate

### Backporting OpenVINO from Fedora 42

Fedora 42+ packages OpenVINO 2024.5.0 which is newer than the bundled OpenVINO 2024.4.4 in intel-npu-acceleration-library 1.4.0, but seems to work OK. The NPU plugin spews warnings but is functional, if and only if the compiler-in-driver component is present.

I have manually enabled building openvino from the F42 package source for F41 in this copr to fill the gap.

### Backporting huggingface-hub from Fedora 42

This was set up in the copr to allow the newer version of huggingface transformers to build on F41.

### Backporting other deps from rawhide

As I work to get these packages into Fedora rawhide (for example in the F43 cycle), I will backport them to F41/F42.

### A note on rust-criterion

It was removed by the Fedora rust-sig as a dev dependency. It's easier just to drop it and any tests that use it.

#### Main TODOs

- The unmodified build process for intel-npu-acceleration-library downloads a binary OpenVINO distribution.
  - It both builds and bundles against that, requiring various changes.
  - Ultimately their weird, non-standard module adding to Python means I have to disable the import test cuz it tries to import the
    native library object as a python module. Maybe that needs to move to lib, lib64, or libexec for the package?
  - Even worse, their OS detection doesn't handle all the prebuilt distros... Oh because only some have NPU support. Sigh.
  - Should probably suggest USE\_SYSTEM\_OPENVINO or something as a fallback upstream.
- On OpenVINO, the good news is that Fedora 42+ packages OpenVINO.
- Numpy v2 is backwards-compatible with numpy v1, so not a big issue, just need to fix packages that specify one or the other.
- a lot of packages need their licenses fixed up to be SPDX
- most of my packages don't correctly annotate licenses, docs, test data, etc right now
- I may need to manually specify deps on packages outside of the python ones?
- the aaaa spec link exists because the default spec for rpkg should be alphabetically first
- neural\_compressor is missing the requirements.txt files in the source distribution, instead they are in the egg-info requires.txt format...
- neural\_compressor only needs the deps because parts of it try to import them, we are currently skipping that check to get it to build
- pycocotools has a randomly-included MIT-licensed C++ JSON parser taken from https://github.com/vivkin/gason at some point. Sigh.
- I need to check the huggingface packages and rust deps for vendored stuff
- for ex, the esaxx-rs crate is Apache-2.0 licensed but it vendors an MIT licensed C++ library. Sigh.
- tokenizers seems to have functions that download random models directly from the internet; these might already be *packaged* in Fedora in huggingface\_hub which IIUC Copr and others use for AI in log-detective? Is the random downloading potentially a problem? Should we be packaging models as well for Fedora? -> Probably a MUCH bigger discussion on the mailing list, frankly...
- did deleting things in neural-compressor (esp.) or acclerate or transformers etc. damage the package rather than just stripping unused stuff?

## Candidates for evaluation for future packaging

Feel free to file bugs to suggest additional candidates.

- [OpenVINO](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) - Is now packaged in Fedora!
- [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel)
- [OpenVINO AI Plugins for GIMP](https://github.com/intel/openvino-ai-plugins-gimp)
- [OpenVINO AI Plugins for Audacity](https://github.com/intel/openvino-plugins-ai-audacity)
- [Intel LLM Library for PyTorch](https://github.com/intel-analytics/ipex-llm)
- [Ollama](https://github.com/ollama/ollama) [(Homepage)](https://ollama.com/) possibly with [OpenWebUI](https://github.com/open-webui/open-webui)
	- Ollama doesn't support the Intel NPU yet, but this setup is very popular for running LLMs locally.
- [Intel's suggestions for using AI on their CPUs/GPUs/NPUs/FPGAs/etc.](https://github.com/intel/edge-developer-kit-reference-scripts)
	- more for additional ideas on what to package since it's just a bunch of docs and distro-specific scripts designed to get people started
