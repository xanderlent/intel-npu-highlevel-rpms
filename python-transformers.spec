Name:           python-transformers
Version:        4.46.3
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


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'transformers' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-transformers
Summary:        %{summary}

%description -n python3-transformers %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-transformers accelerate,ftfy,serving,sklearn,tokenizers,torch,torch-vision,vision


%prep
%autosetup -p1 -n transformers-%{version}
# These files require Tensorflow, so remove them to make the import tests work
# These probably belong to one of the extras we don't package
rm src/transformers/activations_tf.py
rm src/transformers/benchmark/benchmark_tf.py
rm src/transformers/generation/tf_logits_process.py
rm src/transformers/generation/tf_utils.py
rm src/transformers/keras_callbacks.py
rm src/transformers/modeling_tf_outputs.py
rm src/transformers/modeling_tf_utils.py
rm src/transformers/models/albert/modeling_tf_albert.py
rm src/transformers/models/bart/modeling_tf_bart.py
rm src/transformers/models/bert/convert_bert_original_tf2_checkpoint_to_pytorch.py
rm src/transformers/models/bert/convert_bert_pytorch_checkpoint_to_original_tf.py
rm src/transformers/models/bert/convert_bert_token_dropping_original_tf2_checkpoint_to_pytorch.py
rm src/transformers/models/bert/modeling_tf_bert.py
rm src/transformers/models/bert/tokenization_bert_tf.py
rm src/transformers/models/bigbird_pegasus/convert_bigbird_pegasus_tf_to_pytorch.py
rm src/transformers/models/deprecated/gptsan_japanese/convert_gptsan_tf_checkpoint_to_pytorch.py
rm src/transformers/models/efficientnet/convert_efficientnet_to_pytorch.py
rm src/transformers/models/gpt2/tokenization_gpt2_tf.py
rm src/transformers/models/idefics/perceiver_tf.py
rm src/transformers/models/idefics/vision_tf.py
rm src/transformers/models/pegasus/convert_pegasus_tf_to_pytorch.py
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
rm src/transformers/models/fnet/convert_fnet_original_flax_checkpoint_to_pytorch.py
rm src/transformers/models/owlv2/convert_owlv2_to_hf.py
rm src/transformers/models/owlvit/convert_owlvit_original_flax_to_hf.py
rm src/transformers/models/pix2struct/convert_pix2struct_original_pytorch_to_hf.py
rm src/transformers/models/switch_transformers/convert_switch_transformers_original_flax_checkpoint_to_pytorch.py
rm src/transformers/models/t5/convert_t5x_checkpoint_to_pytorch.py
rm src/transformers/models/umt5/convert_umt5_checkpoint_to_pytorch.py
rm src/transformers/models/vivit/convert_vivit_flax_to_pytorch.py
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
# These files needs sentencepiece, which is related to an extra we don't package.
rm src/transformers/models/albert/tokenization_albert.py
rm src/transformers/models/barthez/tokenization_barthez.py
rm src/transformers/models/bartpho/tokenization_bartpho.py
rm src/transformers/models/bert_generation/tokenization_bert_generation.py
rm src/transformers/models/big_bird/tokenization_big_bird.py
rm src/transformers/models/camembert/tokenization_camembert.py
rm src/transformers/models/gemma/modular_gemma.py
rm src/transformers/models/moshi/convert_moshi_transformers.py
# these files using sentencepiece were found with grep and are manually unverified
rm src/transformers/models/code_llama/tokenization_code_llama.py
rm src/transformers/models/cpm/tokenization_cpm.py
rm src/transformers/models/deberta_v2/tokenization_deberta_v2.py
rm src/transformers/models/deprecated/ernie_m/tokenization_ernie_m.py
rm src/transformers/models/deprecated/xlm_prophetnet/tokenization_xlm_prophetnet.py
rm src/transformers/models/fnet/tokenization_fnet.py
rm src/transformers/models/gemma/tokenization_gemma.py
rm src/transformers/models/gpt_sw3/tokenization_gpt_sw3.py
rm src/transformers/models/layoutxlm/tokenization_layoutxlm.py
rm src/transformers/models/llama/tokenization_llama.py
rm src/transformers/models/m2m_100/tokenization_m2m_100.py
rm src/transformers/models/marian/tokenization_marian.py
rm src/transformers/models/mbart50/tokenization_mbart50.py
rm src/transformers/models/mbart/tokenization_mbart.py
rm src/transformers/models/mluke/tokenization_mluke.py
rm src/transformers/models/nllb/tokenization_nllb.py
rm src/transformers/models/pegasus/tokenization_pegasus.py
rm src/transformers/models/plbart/tokenization_plbart.py
rm src/transformers/models/reformer/tokenization_reformer.py
rm src/transformers/models/rembert/tokenization_rembert.py
rm src/transformers/models/seamless_m4t/tokenization_seamless_m4t.py
rm src/transformers/models/siglip/tokenization_siglip.py
rm src/transformers/models/speecht5/tokenization_speecht5.py
rm src/transformers/models/speech_to_text/tokenization_speech_to_text.py
rm src/transformers/models/t5/tokenization_t5.py
rm src/transformers/models/udop/tokenization_udop.py
rm src/transformers/models/xglm/tokenization_xglm.py
rm src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py
rm src/transformers/models/xlnet/tokenization_xlnet.py
# The falcom_mamba kernel needs einops
# These probably belong to one of the extras we don't package
rm -r src/transformers/kernels/falcon_mamba
# Not sure what's missing here, but agents is an extra we don't package?
rm src/transformers/agents/evaluate_agent.py
# Not sure which extra this is from, but align is missing and isn't a dep, so must be an extra
rm src/transformers/models/align/convert_align_tf_to_hf.py
# Needs torchaudio for this extra, not packaged in Fedora
rm src/transformers/models/audio_spectrogram_transformer/convert_audio_spectrogram_transformer_original_to_pytorch.py
rm src/transformers/models/wav2vec2_bert/convert_wav2vec2_seamless_checkpoint.py
# Need bark
rm src/transformers/models/bark/convert_suno_to_hf.py
# Need fairseq
rm src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/data2vec/convert_data2vec_audio_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/data2vec/convert_data2vec_text_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/deprecated/mega/convert_mega_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/fsmt/convert_fsmt_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/hubert/convert_hubert_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/kosmos2/convert_kosmos2_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/roberta/convert_roberta_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/sew/convert_sew_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/sew_d/convert_sew_d_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/speech_encoder_decoder/convert_mbart_wav2vec2_seq2seq_original_to_pytorch.py
rm src/transformers/models/speech_encoder_decoder/convert_speech_to_text_wav2vec2_seq2seq_original_to_pytorch.py
rm src/transformers/models/unispeech/convert_unispeech_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/unispeech_sat/convert_unispeech_sat_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/wav2vec2/convert_wav2vec2_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/wav2vec2_conformer/convert_wav2vec2_conformer_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/xlm_roberta_xl/convert_xlm_roberta_xl_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/xmod/convert_xmod_original_pytorch_checkpoint_to_pytorch.py
# Needs datasets
rm src/transformers/models/beit/convert_beit_unilm_to_pytorch.py
rm src/transformers/models/donut/convert_donut_to_pytorch.py
# Needs timm
rm src/transformers/models/bit/convert_bit_to_pytorch.py
rm src/transformers/models/data2vec/convert_data2vec_vision_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/deit/convert_deit_timm_to_pytorch.py
rm src/transformers/models/deprecated/vit_hybrid/convert_vit_hybrid_timm_to_pytorch.py
rm src/transformers/models/levit/convert_levit_timm_to_pytorch.py
rm src/transformers/models/regnet/convert_regnet_to_pytorch.py
rm src/transformers/models/resnet/convert_resnet_to_pytorch.py
rm src/transformers/models/swin/convert_swin_timm_to_pytorch.py
rm src/transformers/models/swinv2/convert_swinv2_timm_to_pytorch.py
rm src/transformers/models/vit/convert_vit_timm_to_pytorch.py
# Needs lavis
rm src/transformers/models/blip_2/convert_blip_2_original_to_pytorch.py
rm src/transformers/models/instructblip/convert_instructblip_original_to_pytorch.py
rm src/transformers/models/instructblipvideo/convert_instructblipvideo_original_to_pytorch.py
# Needs bros
rm src/transformers/models/bros/convert_bros_to_pytorch.py
# Needs trajectory
rm src/transformers/models/deprecated/trajectory_transformer/convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py
# Needs laion_clap
rm src/transformers/models/clap/convert_clap_original_pytorch_to_hf.py
# Needs clip
rm src/transformers/models/clip/convert_clip_original_pytorch_to_hf.py
# Needs model.blip that isn't transformers.model.blip - I guess that's another original package?
rm src/transformers/models/blip/convert_blip_original_pytorch_to_hf.py
# Needs gluonnlp
rm src/transformers/models/deprecated/bort/convert_bort_original_gluonnlp_checkpoint_to_pytorch.py
# Needs esm
rm src/transformers/models/esm/convert_esm.py
# Needs flatdict
rm src/transformers/models/fuyu/convert_fuyu_model_weights_to_hf.py
rm src/transformers/models/persimmon/convert_persimmon_weights_to_hf.py
# Needs av
rm src/transformers/models/git/convert_git_to_pytorch.py
# Needs s3prl
rm src/transformers/models/hubert/convert_distilhubert_original_s3prl_checkpoint_to_pytorch.py
# Needs pytorch_lightning
rm src/transformers/models/longformer/convert_longformer_original_pytorch_lightning_to_pytorch.py
# Needs t5x
rm src/transformers/models/longt5/convert_longt5x_checkpoint_to_flax.py
rm src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py
# Needs detectron2
rm src/transformers/models/mask2former/convert_mask2former_original_pytorch_checkpoint_to_pytorch.py
rm src/transformers/models/maskformer/convert_maskformer_original_pytorch_checkpoint_to_pytorch.py
# Needs audiocraft
rm src/transformers/models/musicgen/convert_musicgen_transformers.py
rm src/transformers/models/musicgen_melody/convert_musicgen_melody_transformers.py
# Needs nemo
rm src/transformers/models/nemotron/convert_nemotron_nemo_to_hf.py
# Needs nougat
rm src/transformers/models/nougat/convert_nougat_to_hf.py
# Needs haiku
rm src/transformers/models/perceiver/convert_perceiver_haiku_to_pytorch.py
# Needs mistral_common
rm src/transformers/models/pixtral/convert_pixtral_weights_to_hf.py
# The data for this model is missing
rm src/transformers/models/pop2piano/convert_pop2piano_weights_to_hf.py
# Needs pretty_midi
rm src/transformers/models/pop2piano/tokenization_pop2piano.py
# Needs transformers_old
rm src/transformers/models/prophetnet/convert_prophetnet_original_pytorch_checkpoint_to_pytorch.py
# Needs classy_vision
rm src/transformers/models/regnet/convert_regnet_seer_10b_to_pytorch.py
# Needs seamless_communication
rm src/transformers/models/seamless_m4t/convert_fairseq2_to_hf.py
rm src/transformers/models/seamless_m4t_v2/convert_fairseq2_to_hf.py
# Needs tensorstore
rm src/transformers/models/switch_transformers/convert_big_switch.py
# Needs gdown
rm src/transformers/models/timesformer/convert_timesformer_to_pytorch.py
rm src/transformers/models/videomae/convert_videomae_to_pytorch.py
rm src/transformers/models/x_clip/convert_x_clip_original_pytorch_to_hf.py
# Needs unlim
rm src/transformers/models/wavlm/convert_wavlm_original_pytorch_checkpoint_to_pytorch.py
# Needs ipython
rm src/transformers/utils/notebook.py
# Needs google.protobuf.internal
rm src/transformers/utils/sentencepiece_model_pb2_new.py
# This one seems like a pyTorch issue?
# "Dynamo is not supported on Python 3.12+"
rm src/transformers/integrations/bitnet.py
# Internal import error?
rm src/transformers/models/imagegpt/convert_imagegpt_original_tf2_to_pytorch.py
# Some kinda docstring issue?
rm src/transformers/models/llava_next_video/modular_llava_next_video.py
# Uses a tensorflow function that we deleted
rm src/transformers/models/lxmert/convert_lxmert_original_tf_checkpoint_to_pytorch.py
rm src/transformers/models/mt5/modeling_tf_mt5.py
# More import issues/removed functions?
rm src/transformers/models/vit_mae/convert_vit_mae_to_pytorch.py
# Seems to use an internal pytorch function?
rm src/transformers/trainer_seq2seq.py



%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x accelerate,ftfy,serving,sklearn,tokenizers,torch,torch-vision,vision


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l transformers


%check
%pyproject_check_import


%files -n python3-transformers -f %{pyproject_files}
%{_bindir}/transformers-cli


%changelog
%autochangelog
