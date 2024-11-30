# RPM Packages of software for the Intel NPU

The goal of this repository is to provide Fedora packages for software that runs on the Intel NPU at a higher level than the driver. You can find binary packages built from this repository in [my xanderlent/intel-npu-highlevel Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-highlevel/). Hopefully, with effort and care, these packages will eventually find their way upstream, into Fedora proper.

Right now, all of these packages are originally for Python, so they were generated with the [`pyp2spec`](https://github.com/befeleme/pyp2spec) tool. I'm not completely sure how to use it, so I might be missing some steps, but it definitely does not seem as automated as I would like in terms of converting Python packages to RPMs...

## A note on system requirements

If you want to use this software with the Intel NPU, you will need to install the [driver](https://github.com/intel/linux-npu-driver) and have suitable hardware present in your system, which at present is an "Intel Core Ultra"-branded product from Intel's Meteor Lake, Lunar Lake, or Arrow Lake product lines.

I also unofficially maintain the driver packaging in [another project](https://github.com/xanderlent/intel-npu-driver-rpm), with binaries available in [my xanderlent/intel-npu-driver Copr](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-npu-driver/). Follow the directions there
## List of software packaged

- [Intel NPU Acceleration Library](https://github.com/intel/intel-npu-acceleration-library)
	- A Python library for running various AI/ML workloads on the Intel NPU. They also provide some [docs](https://intel.github.io/intel-npu-acceleration-library/index.html).

### Packaged software and dependencies:
- intel-npu-acceleration-library (TODO)
  - neural-compressor (TODO)
    - opencv-python-headless (TODO, shouldn't this be satisfied by the OpenCV Python full package in Fedora???)
    - pycocotools (TODO)
    - tensorflow (only required for +tf) (TODO, but probably not anytime soon)
  - transformers (TODO)
    - tokenizers (downloads rust packages from internet during build)
    - safetensors (TODO)
  - pyroma (only required for +dev)
  - sphinx-book-theme (only required for +dev) (downloads webpack etc. from internet during build)
    - ablog
      - sphinx-automodapi
    - sphinx-examples
    - sphinx-thebe
    - sphinx-togglebutton
    - sphinxcontrib-youtube

### TODOs on those packages

- a lot of packages need their licenses fixed up to be SPDX
- I may need to manually specify deps on packages?
- the aaaa spec link exists because the default spec for rpkg should be alphabetically first
- neural\_compressor is missing the requirements.txt files in the source distribution, instead they are in the egg-info requires.txt format...
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
- tokenizers downloads and compiles a whole smorgasboard of rust code... sigh.
- safetensors downloads and compiles a whole smorgasboard of rust code... sigh.

## Candidates for evaluation for future packaging

Feel free to file bugs to suggest additional candidates.

- [OpenVINO AI Plugins for GIMP](https://github.com/intel/openvino-ai-plugins-gimp)
- [OpenVINO AI Plugins for Audacity](https://github.com/intel/openvino-plugins-ai-audacity)
- [Intel LLM Library for PyTorch](https://github.com/intel-analytics/ipex-llm)
- [Ollama](https://github.com/ollama/ollama) [(Homepage)](https://ollama.com/) possibly with [OpenWebUI](https://github.com/open-webui/open-webui)
	- Ollama doesn't support the Intel NPU yet, but this setup is very popular for running LLMs locally.
- [Intel's suggestions for using AI on their CPUs/GPUs/NPUs/FPGAs/etc.](https://github.com/intel/edge-developer-kit-reference-scripts)
	- more for additional ideas on what to package since it's just a bunch of docs and distro-specific scripts designed to get people started
