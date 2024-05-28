# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# [START documentai_toolbox_convert_external_annotations]

import traceback
from google.cloud.documentai_toolbox import converter

# TODO(developer): Uncomment these variables before running the sample.
# This sample will convert external annotations to the Document.json format used by Document AI Workbench for training.
# To process this the external annotation must have these type of objects:
#       1) Type
#       2) Text
#       3) Bounding Box (bounding boxes must be 1 of the 3 optional types)
#
# This is the bare minimum requirement to convert the annotations but for better accuracy you will need to also have:
#       1) Document width & height
#
# Bounding Box Types:
#   Type 1:
#       bounding_box:[{"x":1,"y":2},{"x":2,"y":2},{"x":2,"y":3},{"x":1,"y":3}]
#   Type 2:
#       bounding_box:{ "Width": 1, "Height": 1, "Left": 1, "Top": 1}
#   Type 3:
#       bounding_box: [1,2,2,2,2,3,1,3]
#
#   Note: If these types are not sufficient you can propose a feature request or contribute the new type and conversion functionality.
#
# Given a folders in gcs_input_path with the following structure :
#
# gs://path/to/input/folder
#   ├──test_annotations.json
#   ├──test_config.json
#   └──test.pdf
#  guid1_annotations.json
#  guid1.pdf
#  ------
#  gcs_input_dir/config.json
#  gcs_input_dir/guid1_annotations.json
#  gcs_input_dir/guid1.pdf
# 
#
# An example of the config is in sample-converter-configs/Azure/form-config.json
#
location = "us",
processor_id = "ff4c4a2da05451b0"
gcs_input_path = "gs://reside-stage-docai/nic-docai-toolbox-py-tests/test1"
gcs_output_path = "gs://reside-stage-docai/nic-docai-toolbox-py-tests-output/test1"
project_id = "reside-stage"

try:
    converter.convert_from_config(
        project_id=project_id,
        location=location,
        processor_id=processor_id,
        gcs_input_path=gcs_input_path,
        gcs_output_path=gcs_output_path,
    )
except Exception as e:
    error_msg = f'Error processing {e}'
    print(f'{error_msg}\n{traceback.format_exc()}')

# [END documentai_toolbox_convert_external_annotations]
