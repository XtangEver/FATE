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
from pyspark import RDD

from fate_arch.abc import AddressABC, CTableABC

# noinspection PyAbstractClass
class Table(CTableABC):
    def __init__(self, rdd: RDD):
        self._rdd: RDD = ...
        ...
    def save(self, address: AddressABC, partitions: int, schema: dict, **kwargs): ...

def from_hdfs(paths: str, partitions) -> Table: ...
def from_hive(tb_name: str, db_name: str, partitions: int) -> Table: ...
def from_rdd(rdd) -> Table: ...
