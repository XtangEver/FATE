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
from flask import Flask, request

from fate_arch.common import conf_utils
from fate_flow.entity.runtime_config import RuntimeConfig
from fate_flow.settings import stat_logger
from fate_flow.utils.api_utils import get_json_result
from fate_flow.utils.service_utils import ServiceUtils

manager = Flask(__name__)


@manager.errorhandler(500)
def internal_server_error(e):
    stat_logger.exception(e)
    return get_json_result(retcode=100, retmsg=str(e))


@manager.route('/get', methods=['POST'])
def get_fate_version_info():
    version = RuntimeConfig.get_env(request.json.get('module', 'FATE'))
    return get_json_result(data={request.json.get('module'): version})


@manager.route('/registry', methods=['POST'])
def service_registry():
    update_server = ServiceUtils.register_service(request.json)
    return get_json_result(data={"update_server": update_server})


@manager.route('/query', methods=['POST'])
def service_query():
    service_info = ServiceUtils.get(request.json.get("service_name"))
    return get_json_result(data={"service_info": service_info})