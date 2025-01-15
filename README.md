# RPM Packages of software for the Intel NPU

The goal of this repository is to provide Fedora packages for software that runs on the Intel NPU at a higher level than the driver. You can find binary packages built from this repository in [my xanderlent/intel-npu-highlevel Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-highlevel/).

Because this repo happens to provide many AI/ML packages not yet upstream in Fedora, I have also enabled aarch64 builds where possible. (I am not adverse to enabling ppc64le or s390x builds, or even 32-bit compatability builds; If you want me to enable said builds, please create an Issue requesting them.)

Hopefully, with effort and care, these packages will eventually find their way upstream, into Fedora proper. (For now, the Fedora Review step has been disabled in copr to improve build times.) Perhaps the place to start would be with the Fedora AI/ML SIG?

Right now, most of these packages are originally for Python, so they were generated with the [`pyp2spec`](https://github.com/befeleme/pyp2spec) tool. I'm not completely sure how to use it, so I might be missing some steps, but it definitely does not seem as automated as I would like in terms of converting Python packages to RPMs... On the other hand, [rust2rpm](https://pagure.io/fedora-rust/rust2rpm) was a breeze to use. (`rust2rpm --no-rpmautospec -t fedora --compat crate@version`, leave out `--compat` for non-versioned packages.)

## A note on system requirements

If you want to use this software with the Intel NPU, you will need to install the [driver](https://github.com/intel/linux-npu-driver) and have suitable hardware present in your system, which at present is an "Intel Core Ultra"-branded product from Intel's Meteor Lake, Lunar Lake, or Arrow Lake product lines.

I also unofficially maintain the driver packaging in [another project](https://github.com/xanderlent/intel-npu-driver-rpm), with binaries available in [my xanderlent/intel-npu-driver Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-driver/). Follow the directions there
## List of software packaged

- [Intel NPU Acceleration Library](https://github.com/intel/intel-npu-acceleration-library)
	- A Python library for running various AI/ML workloads on the Intel NPU. They also provide some [docs](https://intel.github.io/intel-npu-acceleration-library/index.html).

### Packaged software and dependencies:
- python-intel-npu-acceleration-library (TODO: The only remaining TODO!)
  - python-neural-compressor (+pt)
    - python-accelerate
      - python-safetensors (+numpy,+torch)
    - (opencv-python-headlesswas substituted with packaged opencv)
    - python-pycocotools
      - (oldest-supported-numpy was substituted with packaged numpy)
    - python-transformers (see below)
  - python-transformers (+accelerate,+ftfy,+sentencepiece,+serving,+sklearn,+tokenizers,+torch,+torch-vision,+vision; future work for +onnx{,runtime},+modelcreation)
    - python-accelerate (see above)
      - python-safetensors (see above)
    - python-tokenizers (+docs)
      - rust-esaxx-rs
        - rust-criterion (see notes for F41+)
      - rust-macro\_rules\_attribute
        - rust-macro\_rules\_attribute-proc\_macro
      - rust-monostate
        - rust-monostate-impl
      - rust-ndarray0.15
        - rust-approx0.4
      - rust-numpy
        - rust-nalgebra0.32 (this subtree built on Fedora 41+ only)
          - rust-criterion0.4 (uses most of the same deps as rust-criterion, as well as rust-approx0.4)
          - rust-simba0.8
      - rust-rayon-cond
      - rust-spm\_precompiled
      - rust-unicode-normalization-alignments
    - python-safetensors (see above)

### Revived orphaned deps of rust-criterion from F40

In F41+, various deps of rust-criterion were removed. Rather than vendoring them all here, I have set up
the copr system to build them for F41+ based on the code last used in f40. While eventually these versions
will get stale, we can keep these orphaned leaf packages alive a little longer.

(Fedora removed rust-criterion itself as an orphaned leaf in F38+, so we vendor it here since the version in
dist-git is old.)

  - rust-anes
  - rust-criterion-plot
    - rust-itertools-num
  - rust-oorandom
    - rust-random-fast-rng
      - rust-random-trait
    - rust-randomize
  - rust-plotters
    - rust-plotters-backend
    - rust-plotters-bitmap
      - rust-gif0.12 (of these, the only one in this tree, built on Fedora 41+ only)
      - rust-plotters-backend
    - rust-plotters-svg
      - rust-plotters-backend
  - rust-tinytemplate

### TODOs on those packages

#### Main TODOs

- The build process for intel-npu-acceleration-library downloads a binary OpenVINO distribution and both bundles and builds against that. Yikes, Intel!
  - Even worse, their OS detection doesn't handle all the prebuilt distros... Oh because only some have NPU support. Sigh.
  - I might package OpenVINO in it's own COPR or repo, or even the main repo since it can integrate tightly with the driver.
- Apparently Fedora 42+ isn't yet packaging numpy v1, so builds of python-neural-compressor are failing in rawhide?
  - Not sure if this is another temporary rawhide fail or something permanent, since other numpy-based packages built in the past?
  - maybe those have multiple paths for v1/v2 though
  - seems like the numpy v2 transition is generally a big deal
- a lot of packages need their licenses fixed up to be SPDX
- most of my packages don't correctly annotate licenses, docs, test data, etc right now
- I may need to manually specify deps on packages outside of the python ones?
- the aaaa spec link exists because the default spec for rpkg should be alphabetically first
- neural\_compressor is missing the requirements.txt files in the source distribution, instead they are in the egg-info requires.txt format...
- neural\_compressor only needs the deps because parts of it try to import them, we are currently skipping that check to get it to build
- pycocotools <= 2.0.7 is needed to work with numpy 1.x which Fedora is shipping, also the numpy dependency needs to be tweaked with sed
- pycocotools has a randomly-included MIT-licensed C++ JSON parser taken from https://github.com/vivkin/gason at some point. Sigh.
- tokenizers needs some rust deps I haven't figured out
- safetensors the rust package seems to already be packaged in Fedora; can we add these bindings to that package rather than recompile?
- tokenizers seems similar; while it's a rust lib primirally used through python, we should probably try to build it once with bindings etc?
- I need to check the huggingface packages and rust deps for vendored stuff
- for ex, the esaxx-rs crate is Apache-2.0 licensed but it vendors an MIT licensed C++ library. Sigh.
- tokenizers seems to have functions that download random models directly from the internet; these might already be *packaged* in Fedora in huggingface\_hub which IIUC Copr and others use for AI in log-detective? Is the random downloading potentially a problem? Should we be packaging models as well for Fedora? -> Probably a MUCH bigger discussion on the mailing list, frankly...
- the criterion package tweaks a tight version bound on a tool to allow supposedly-compatible versions based on semver
- rust-gif0.12 needs to be built without check since that creates a circular dep on rust-criterion
- did deleting things in neural-compressor (esp.) or acclerate or transformers etc. damage the package rather than just stripping unused stuff?

## Candidates for evaluation for future packaging

Feel free to file bugs to suggest additional candidates.

- [OpenVINO](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) itself?
- [OpenVINO AI Plugins for GIMP](https://github.com/intel/openvino-ai-plugins-gimp)
- [OpenVINO AI Plugins for Audacity](https://github.com/intel/openvino-plugins-ai-audacity)
- [Intel LLM Library for PyTorch](https://github.com/intel-analytics/ipex-llm)
- [Ollama](https://github.com/ollama/ollama) [(Homepage)](https://ollama.com/) possibly with [OpenWebUI](https://github.com/open-webui/open-webui)
	- Ollama doesn't support the Intel NPU yet, but this setup is very popular for running LLMs locally.
- [Intel's suggestions for using AI on their CPUs/GPUs/NPUs/FPGAs/etc.](https://github.com/intel/edge-developer-kit-reference-scripts)
	- more for additional ideas on what to package since it's just a bunch of docs and distro-specific scripts designed to get people started
