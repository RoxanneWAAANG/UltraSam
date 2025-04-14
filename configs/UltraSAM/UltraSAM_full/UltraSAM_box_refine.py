_base_ = [
    '../../_base_/datasets/sam_dataset_bbox_prompt.py',
    '../../_base_/models/sam_mask_refinement.py'
    ]

data_root = '/home/jack/Projects/yixin-llm/yixin-llm-data/UltraSam/dataset/AUL'

train_dataloader = dict(
    batch_size=8,
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='images'),
        ann_file='annotations/AUL__coco.json',
        test_mode=True,
    ),
)

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='images'),
        ann_file='annotations/AUL__coco.json',
        test_mode=True,
    ),
)

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img='images'),
        ann_file='annotations/AUL__coco.json',
        test_mode=True,
    ),
)

orig_val_evaluator = _base_.val_evaluator
orig_val_evaluator['ann_file'] = '{}/annotations/AUL__coco.json'.format(data_root)
val_evaluator = orig_val_evaluator

orig_test_evaluator = _base_.test_evaluator
orig_test_evaluator['ann_file'] = '{}/annotations/AUL__coco.json'.format(data_root)
test_evaluator = orig_test_evaluator
