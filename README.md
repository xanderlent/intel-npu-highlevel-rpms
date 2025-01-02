# RPM Packages of software for the Intel NPU

The goal of this repository is to provide Fedora packages for software that runs on the Intel NPU at a higher level than the driver. You can find binary packages built from this repository in [my xanderlent/intel-npu-highlevel Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-highlevel/). Hopefully, with effort and care, these packages will eventually find their way upstream, into Fedora proper.

Right now, most of these packages are originally for Python, so they were generated with the [`pyp2spec`](https://github.com/befeleme/pyp2spec) tool. I'm not completely sure how to use it, so I might be missing some steps, but it definitely does not seem as automated as I would like in terms of converting Python packages to RPMs... On the other hand, [rust2rpm](https://pagure.io/fedora-rust/rust2rpm) was a breeze to use.

## A note on system requirements

If you want to use this software with the Intel NPU, you will need to install the [driver](https://github.com/intel/linux-npu-driver) and have suitable hardware present in your system, which at present is an "Intel Core Ultra"-branded product from Intel's Meteor Lake, Lunar Lake, or Arrow Lake product lines.

I also unofficially maintain the driver packaging in [another project](https://github.com/xanderlent/intel-npu-driver-rpm), with binaries available in [my xanderlent/intel-npu-driver Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-driver/). Follow the directions there
## List of software packaged

- [Intel NPU Acceleration Library](https://github.com/intel/intel-npu-acceleration-library)
	- A Python library for running various AI/ML workloads on the Intel NPU. They also provide some [docs](https://intel.github.io/intel-npu-acceleration-library/index.html).

### Packaged software and dependencies:
- intel-npu-acceleration-library (TODO)
  - neural-compressor (with +pt extra, since torch is already packaged in Fedora, but without +tf since Tensorflow isn't) (TODO)
    - opencv-python-headless (substituted with packaged opencv)
    - pycocotools
      - oldest-supported-numpy (substituted with packaged numpy)
    - transformers (TODO)
  - transformers (TODO)
    - tokenizers (TODO)
      - rust-numpy (TODO: Needs nalgebra ^0.32 which isn't packaged in F41+.)
      - rust-macro\_rules\_attribute
        - rust-macro\_rules\_attribute-proc\_macro
      - rust-monostate
        - rust-monostate-impl
      - rust-rayon-cond
      - rust-spm\_precompiled
      - rust-esaxx-rs
        - rust-criterion (TODO: All the dependencies were orphaned leaves and removed from F41+. Also only a dev dependency?)
    - safetensors (+numpy,+torch extras, since they're in Fedora, but without other extras like Tensorflow)
  - pyroma (only required for +dev)
  - sphinx-book-theme (only required for +dev)
    - ablog
      - sphinx-automodapi
    - sphinx-examples
    - sphinx-thebe
    - sphinx-togglebutton
    - sphinxcontrib-youtube

### TODOs on those packages

#### Main TODOs

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
- I need to check the huggingface packages and rust deps for vendored stuff
- for ex, the esaxx-rs crate is Apache-2.0 licensed but it vendors an MIT licensed C++ library. Sigh.

#### TODOs for building intel-npu-acceleration-library with +dev

- pyroma and zest.releaser have a circular dependency, if pyroma's test extra is built, so exclude it in the conf file
- ablog >0.11.8 requires deps that are too new!
- sphinx-automodapi, old version needed because newer versions require newer sphinx
- sphinx-automodapi needs the archive name modified in the spec file from _ to -
- sphinx-examples has the URL issue with PyPI again...
- sphinx-examples with extra sphinx has a circular dependency on sphinx-book-theme
- sphinx-examples needs the archive name modified in the spec file from _ to -
- sphinx-thebe with extra sphinx has a circular dependency on sphinx-book-theme
- sphinx-togglebutton with extra sphinx has a circular dep on sphinx-book-theme
- sphinx-book-theme seems to download NPM packages during the build... really?

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
