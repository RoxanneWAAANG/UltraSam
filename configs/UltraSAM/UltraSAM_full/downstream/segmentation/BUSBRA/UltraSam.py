# _base_ = [
#     '../../../../../_base_/datasets/sam_dataset_segmentation.py',
#     '../../../../../_base_/models/mask2former_sam.py'
# ]
_base_ = [
    '../../../../../_base_/datasets/sam_dataset_bbox_prompt.py',
    '../../../../../_base_/models/sam.py'
]

data_root = '/home/jack/Projects/yixin-llm/yixin-llm-data/UltraSam/dataset/BrEaST/BrEaST-Lesions_USG-images_and_masks-Dec-15-2023'

classes = ('breast_nodule', 'cyst')

# model = dict(
#     backbone=dict(
#         init_cfg=dict(prefix="backbone.", checkpoint="weights/UltraSam.pth")
#     ),
#     panoptic_head=dict(
#         num_things_classes=len(classes),
#         loss_cls=dict(
#             class_weight=[1.0] * len(classes) + [0.1]
#         ),
#     ),
#     panoptic_fusion_head=dict(
#         num_things_classes=len(classes),
#     ),
# )
model = dict(use_mask_refinement=True)

train_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo={'classes': classes},
        data_prefix=dict(img='images'),
        ann_file='annotations/BrEaST-Lesions_USG-images_and_masks-Dec-15-2023__coco.json',
    ),
)

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo={'classes': classes},
        data_prefix=dict(img='images'),
        ann_file='annotations/BrEaST-Lesions_USG-images_and_masks-Dec-15-2023__coco.json',
        test_mode=True,
    ),
)

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo={'classes': classes},
        data_prefix=dict(img='images'),
        ann_file='annotations/BrEaST-Lesions_USG-images_and_masks-Dec-15-2023__coco.json',
        test_mode=True,
    ),
)

orig_val_evaluator = _base_.val_evaluator
orig_val_evaluator['ann_file'] = '{}/annotations/BrEaST-Lesions_USG-images_and_masks-Dec-15-2023__coco.json'.format(data_root)
val_evaluator = orig_val_evaluator

orig_test_evaluator = _base_.test_evaluator
orig_test_evaluator['ann_file'] = '{}/annotations/BrEaST-Lesions_USG-images_and_masks-Dec-15-2023__coco.json'.format(data_root)
test_evaluator = orig_test_evaluator

# -------------------- Visualizer --------------------
vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='TensorboardVisBackend')
]

visualizer = dict(
    type='DetLocalVisualizer',
    vis_backends=vis_backends,
    name='visualizer'
)

log_processor = dict(type='LogProcessor', window_size=50, by_epoch=False)

log_level = 'INFO'
load_from = None
resume = False
