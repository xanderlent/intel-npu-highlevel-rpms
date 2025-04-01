Name:           python-transformers
Version:        4.50.3
Release:        1%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/transformers
Source:         %{pypi_source transformers}

BuildArch:      noarch
BuildRequires:  python3-devel
# gcc is needed for transformers.models.deprecated.graphormer.algos_graphormer
BuildRequires:	gcc
# rich was? needed for transformers.commands.chat
#BuildRequires:	python3dist(rich)
#Requires:	python3dist(rich)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'transformers' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-transformers
Summary:        %{summary}

%description -n python3-transformers %_description

%if 0%{?fedora} > 41
%pyproject_extras_subpkg -n python3-transformers accelerate,ftfy,num2words,optuna,sentencepiece,serving,sklearn,tiktoken,tokenizers,torch,torch-vision,torchhub,vision
%else
# Fedora 40 doesn't have optuna
%pyproject_extras_subpkg -n python3-transformers accelerate,ftfy,num2words,sentencepiece,serving,sklearn,tiktoken,tokenizers,torch,torch-vision,torchhub,vision
%endif


%prep
%autosetup -p1 -n transformers-%{version}
# These files require Tensorflow, so remove them to make the import tests work
# These probably belong to one of the extras we don't package
rm src/transformers/activations_tf.py
rm src/transformers/generation/tf_logits_process.py
rm src/transformers/generation/tf_utils.py
rm src/transformers/keras_callbacks.py
rm src/transformers/modeling_tf_outputs.py
rm src/transformers/modeling_tf_utils.py
rm src/transformers/models/albert/modeling_tf_albert.py
rm src/transformers/models/bart/modeling_tf_bart.py
rm src/transformers/models/bert/modeling_tf_bert.py
rm src/transformers/models/bert/tokenization_bert_tf.py
rm src/transformers/models/gpt2/tokenization_gpt2_tf.py
rm src/transformers/models/idefics/perceiver_tf.py
rm src/transformers/models/idefics/vision_tf.py
rm src/transformers/optimization_tf.py
rm src/transformers/tf_utils.py
# these Tensorflow exclusions are found with grep and are manually unverified
rm src/transformers/models/blenderbot/modeling_tf_blenderbot.py
rm src/transformers/models/blenderbot_small/modeling_tf_blenderbot_small.py
rm src/transformers/models/blip/modeling_tf_blip.py
rm src/transformers/models/blip/modeling_tf_blip_text.py
rm src/transformers/models/camembert/modeling_tf_camembert.py
rm src/transformers/models/clip/modeling_tf_clip.py
rm src/transformers/models/convbert/modeling_tf_convbert.py
rm src/transformers/models/convnext/modeling_tf_convnext.py
rm src/transformers/models/convnextv2/modeling_tf_convnextv2.py
rm src/transformers/models/ctrl/modeling_tf_ctrl.py
rm src/transformers/models/cvt/modeling_tf_cvt.py
rm src/transformers/models/data2vec/modeling_tf_data2vec_vision.py
rm src/transformers/models/deberta/modeling_tf_deberta.py
rm src/transformers/models/deberta_v2/modeling_tf_deberta_v2.py
rm src/transformers/models/deit/modeling_tf_deit.py
rm src/transformers/models/deprecated/efficientformer/modeling_tf_efficientformer.py
rm src/transformers/models/deprecated/transfo_xl/modeling_tf_transfo_xl.py
rm src/transformers/models/deprecated/transfo_xl/modeling_tf_transfo_xl_utilities.py
rm src/transformers/models/distilbert/modeling_tf_distilbert.py
rm src/transformers/models/dpr/modeling_tf_dpr.py
rm src/transformers/models/electra/modeling_tf_electra.py
rm src/transformers/models/encoder_decoder/modeling_tf_encoder_decoder.py
rm src/transformers/models/esm/modeling_tf_esm.py
rm src/transformers/models/flaubert/modeling_tf_flaubert.py
rm src/transformers/models/funnel/modeling_tf_funnel.py
rm src/transformers/models/gpt2/modeling_tf_gpt2.py
rm src/transformers/models/gptj/modeling_tf_gptj.py
rm src/transformers/models/groupvit/modeling_tf_groupvit.py
rm src/transformers/models/hubert/modeling_tf_hubert.py
rm src/transformers/models/idefics/modeling_tf_idefics.py
rm src/transformers/models/layoutlm/modeling_tf_layoutlm.py
rm src/transformers/models/layoutlmv3/modeling_tf_layoutlmv3.py
rm src/transformers/models/led/modeling_tf_led.py
rm src/transformers/models/longformer/modeling_tf_longformer.py
rm src/transformers/models/lxmert/modeling_tf_lxmert.py
rm src/transformers/models/marian/modeling_tf_marian.py
rm src/transformers/models/mbart/modeling_tf_mbart.py
rm src/transformers/models/mistral/modeling_tf_mistral.py
rm src/transformers/models/mobilebert/modeling_tf_mobilebert.py
rm src/transformers/models/mobilevit/modeling_tf_mobilevit.py
rm src/transformers/models/mpnet/modeling_tf_mpnet.py
rm src/transformers/models/openai/modeling_tf_openai.py
rm src/transformers/models/opt/modeling_tf_opt.py
rm src/transformers/models/pegasus/modeling_tf_pegasus.py
rm src/transformers/models/rag/modeling_tf_rag.py
rm src/transformers/models/regnet/modeling_tf_regnet.py
rm src/transformers/models/rembert/modeling_tf_rembert.py
rm src/transformers/models/resnet/modeling_tf_resnet.py
rm src/transformers/models/roberta/modeling_tf_roberta.py
rm src/transformers/models/roberta_prelayernorm/modeling_tf_roberta_prelayernorm.py
rm src/transformers/models/roformer/modeling_tf_roformer.py
rm src/transformers/models/sam/modeling_tf_sam.py
rm src/transformers/models/segformer/modeling_tf_segformer.py
rm src/transformers/models/speech_to_text/modeling_tf_speech_to_text.py
rm src/transformers/models/swiftformer/modeling_tf_swiftformer.py
rm src/transformers/models/swin/modeling_tf_swin.py
rm src/transformers/models/t5/modeling_tf_t5.py
rm src/transformers/models/tapas/modeling_tf_tapas.py
rm src/transformers/models/vision_encoder_decoder/modeling_tf_vision_encoder_decoder.py
rm src/transformers/models/vision_text_dual_encoder/modeling_tf_vision_text_dual_encoder.py
rm src/transformers/models/vit_mae/modeling_tf_vit_mae.py
rm src/transformers/models/vit/modeling_tf_vit.py
rm src/transformers/models/wav2vec2/modeling_tf_wav2vec2.py
rm src/transformers/models/whisper/modeling_tf_whisper.py
rm src/transformers/models/xglm/modeling_tf_xglm.py
rm src/transformers/models/xlm/modeling_tf_xlm.py
rm src/transformers/models/xlm_roberta/modeling_tf_xlm_roberta.py
rm src/transformers/models/xlnet/modeling_tf_xlnet.py
# These files require jax or flax, so remove them to make the import tests work
# These probably belong to one of the extras we don't package
rm src/transformers/generation/flax_logits_process.py
rm src/transformers/generation/flax_utils.py
rm src/transformers/modeling_flax_outputs.py
rm src/transformers/modeling_flax_pytorch_utils.py
rm src/transformers/modeling_flax_utils.py
rm src/transformers/models/albert/modeling_flax_albert.py
rm src/transformers/models/bart/modeling_flax_bart.py
rm src/transformers/models/beit/modeling_flax_beit.py
rm src/transformers/models/bert/modeling_flax_bert.py
rm src/transformers/models/big_bird/modeling_flax_big_bird.py
# these jax/flax exclusions are found with grep, and are manually unverified
rm src/transformers/models/blenderbot/modeling_flax_blenderbot.py
rm src/transformers/models/blenderbot_small/modeling_flax_blenderbot_small.py
rm src/transformers/models/bloom/modeling_flax_bloom.py
rm src/transformers/models/clip/modeling_flax_clip.py
rm src/transformers/models/dinov2/modeling_flax_dinov2.py
rm src/transformers/models/distilbert/modeling_flax_distilbert.py
rm src/transformers/models/electra/modeling_flax_electra.py
rm src/transformers/models/encoder_decoder/modeling_flax_encoder_decoder.py
rm src/transformers/models/gemma/modeling_flax_gemma.py
rm src/transformers/models/gpt2/modeling_flax_gpt2.py
rm src/transformers/models/gptj/modeling_flax_gptj.py
rm src/transformers/models/gpt_neo/modeling_flax_gpt_neo.py
rm src/transformers/models/llama/modeling_flax_llama.py
rm src/transformers/models/longt5/modeling_flax_longt5.py
rm src/transformers/models/marian/modeling_flax_marian.py
rm src/transformers/models/mbart/modeling_flax_mbart.py
rm src/transformers/models/mistral/modeling_flax_mistral.py
rm src/transformers/models/mt5/modeling_flax_mt5.py
rm src/transformers/models/opt/modeling_flax_opt.py
rm src/transformers/models/pegasus/modeling_flax_pegasus.py
rm src/transformers/models/regnet/modeling_flax_regnet.py
rm src/transformers/models/resnet/modeling_flax_resnet.py
rm src/transformers/models/roberta/modeling_flax_roberta.py
rm src/transformers/models/roberta_prelayernorm/modeling_flax_roberta_prelayernorm.py
rm src/transformers/models/roformer/modeling_flax_roformer.py
rm src/transformers/models/speech_encoder_decoder/modeling_flax_speech_encoder_decoder.py
rm src/transformers/models/t5/modeling_flax_t5.py
rm src/transformers/models/vision_encoder_decoder/modeling_flax_vision_encoder_decoder.py
rm src/transformers/models/vision_text_dual_encoder/modeling_flax_vision_text_dual_encoder.py
rm src/transformers/models/vit/modeling_flax_vit.py
rm src/transformers/models/wav2vec2/modeling_flax_wav2vec2.py
rm src/transformers/models/whisper/modeling_flax_whisper.py
rm src/transformers/models/xglm/modeling_flax_xglm.py
rm src/transformers/models/xlm_roberta/modeling_flax_xlm_roberta.py
# The falcom_mamba kernel needs einops
# These probably belong to one of the extras we don't package
rm -r src/transformers/kernels/falcon_mamba
# Not sure what's missing here, but agents is an extra we don't package?
rm src/transformers/agents/evaluate_agent.py
# Needs trajectory
rm -r src/transformers/models/deprecated/trajectory_transformer/
# Needs pretty_midi
rm src/transformers/models/pop2piano/tokenization_pop2piano.py
# Needs ipython
rm src/transformers/utils/notebook.py
# Needs google.protobuf
rm src/transformers/utils/sentencepiece_model_pb2_new.py
rm src/transformers/utils/sentencepiece_model_pb2.py
# Some kinda docstring issue?
rm src/transformers/models/llava_next_video/modular_llava_next_video.py
# Uses a tensorflow function that we deleted
rm src/transformers/models/mt5/modeling_tf_mt5.py
# Seems to use an internal pytorch function?
rm src/transformers/trainer_seq2seq.py
# Transformers needs the triton library to import this
rm src/transformers/integrations/finegrained_fp8.py
# This integration needs vptq
rm src/transformers/integrations/vptq.py
# This model fails in the import test because of a None docstring?
rm src/transformers/models/aria/modular_aria.py
# This file fails the import test because it's imports are too relative?
rm src/transformers/models/dinov2_with_registers/modular_dinov2_with_registers.py
# Again docstring issues
rm src/transformers/models/got_ocr2/modular_got_ocr2.py
# More None docstrings
rm src/transformers/models/gpt_neox/modular_gpt_neox.py
# Another docstring error
rm src/transformers/models/moonshine/modular_moonshine.py
# More misery with docstrings
rm src/transformers/models/starcoder2/modular_starcoder2.py
# These files use torch.compile, but that doesn't work with the combinations of new python and newish torch packaged
# "Dynamo is not supported on Python <whatever>"
# TODO: Will we ever be able to support this given how it lags behind the rest of PyTorch?
rm src/transformers/integrations/bitnet.py
rm src/transformers/models/modernbert/modeling_modernbert.py
rm src/transformers/models/modernbert/modular_modernbert.py
# Fixup a type error that only shows up when directly importing something as a test that we probably shouldn't
sed -i "s/GEMMA3_INPUTS_DOCSTRING = None/GEMMA3_INPUTS_DOCSTRING = \"\"/" src/transformers/models/gemma3/modular_gemma3.py
# Fixup another silly docstring automation error
sed -i "288d" src/transformers/models/prompt_depth_anything/modular_prompt_depth_anything.py


%generate_buildrequires
%if 0%{?fedora} > 41
%pyproject_buildrequires -x accelerate,ftfy,num2words,optuna,sentencepiece,serving,sklearn,tiktoken,tokenizers,torch,torch-vision,torchhub,vision
%else
# Fedora 40 doesn't have optuna
%pyproject_buildrequires -x accelerate,ftfy,num2words,sentencepiece,serving,sklearn,tiktoken,tokenizers,torch,torch-vision,torchhub,vision
%endif


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l transformers


%check
%pyproject_check_import


%files -n python3-transformers -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/transformers-cli


%changelog
%autochangelog
