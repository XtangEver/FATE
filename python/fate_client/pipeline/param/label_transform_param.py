#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from pipeline.param.base_param import BaseParam


class LabelTransformParam(BaseParam):
    """
    Define label transform param that used in label transform.

    Parameters
    ----------

    label_encoder : None, dict, default : None
        Specify (label, encoded label) key-value pairs for transforming labels to new values.

    need_run: bool, default: True
        Specify whether to run label transform

    """

    def __init__(self, label_encoder=None, need_run=True):
        super(LabelTransformParam, self).__init__()
        self.label_encoder = label_encoder
        self.need_run = need_run

    def check(self):
        model_param_descr = "label transform param's "

        BaseParam.check_boolean(self.need_run, f"{model_param_descr} need run ")

        if self.label_encoder is not None:
            if not isinstance(self.label_encoder, dict):
                raise ValueError(f"{model_param_descr} label_encoder should be dict type")

        LOGGER.debug("Finish label transformer parameter check!")
        return True
