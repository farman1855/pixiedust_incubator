# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from pixiedust.display.display import *
from pixiedust.display import *
from .learningDisplay import PixieDustLearningDisplay
        
class PixieDustLearningPluginMeta(DisplayHandlerMeta):
    @addId
    def getMenuInfo(self,entity):
        if entity==PixieDustLearningPluginMeta:
            return [
                {"categoryId": "Learning", "title": "Course", "icon": "fa-table", "id": "davidTest"}
            ]
        else:
            return []
    def newDisplayHandler(self,options,entity):
        return PixieDustLearningDisplay(options,entity)
    
registerDisplayHandler(PixieDustLearningPluginMeta())


def startCourse():
    display(PixieDustLearningPluginMeta)

def getCourseCells(topic):
    print("hello wolrd")