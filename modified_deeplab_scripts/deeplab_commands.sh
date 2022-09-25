IMAGE_FOLDER="/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/JPEGImages"
LIST_FOLDER="/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/ImageSets/Segmentation"
SEMANTIC_SEG_FOLDER="/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/SegmentationClassRaw"
echo "Converting Binary dataset..."
python3 "/Users/aizazansari/Desktop/models/research/deeplab/datasets/build_voc2012_data.py" \
  --image_folder="${IMAGE_FOLDER}" \
  --semantic_segmentation_folder="${SEMANTIC_SEG_FOLDER}" \
  --list_folder="${LIST_FOLDER}" \
  --image_format="png" \
  --output_dir="/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/tfrecord"

#navigate to the directory where deeplab is stored
cd Desktop/models/research
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

# Set up the working environment.
CURRENT_DIR=$(pwd)
WORK_DIR="${CURRENT_DIR}/deeplab"


python "${WORK_DIR}"/train.py \
    --logtostderr \
    --training_number_of_steps=100 \
    --train_split="train" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size=513,513 \
    --train_batch_size=4 \
    --dataset="bag_dataset" \
    --tf_initial_checkpoint="/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/deeplabv3_xception_ade20k_train/model.ckpt" \
    --train_logdir='//Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/training_checkpoint' \
    --dataset_dir='/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/tfrecord' \
    --initialize_last_layer=False \
    --last_layers_contain_logits_only=True \
    --fine_tune_batch_norm=False \
    --base_learning_rate=0.001

#eval script does not work. use accuracy.ipnyb to evaluate
python deeplab/eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --eval_crop_size=113,118 \
    --dataset="bag_dataset" \
    --checkpoint_dir='/home/deebthik/Downloads/models-master/research/deeplab/datasets/custom_datasets/training_checkpoint_files' \
    --eval_logdir='/home/deebthik/Downloads/models-master/research/deeplab/datasets/custom_datasets/evaluation' \
    --dataset_dir='/home/deebthik/Downloads/models-master/research/deeplab/datasets/custom_datasets/tfrecord'

python "${WORK_DIR}"/vis.py \
    --logtostderr \
    --vis_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size=513,513 \
    --dataset="bag_dataset" \
    --colormap_type="pascal" \
    --checkpoint_dir='/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/training_checkpoint' \
    --vis_logdir='/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/visualization' \
    --dataset_dir='/Users/aizazansari/Desktop/models/research/deeplab/datasets/custom_datasets/tfrecord' 


