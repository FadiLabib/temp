# Copyright 2016 Google Inc.
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

from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ title, author, ingred_list, prep_time, skill_lv, descrip ]
    where title, author, ingred_list, prep_time, skill_lv
    and descrip are python strings
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['title'],entity['author'],entity['ingred_list'],entity['prep_time'], entity['skill_lv'], entity['descrip']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs410c-fadi-labib')

    def select(self):
        query = self.client.query(kind = 'Recipe')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def select_translated(self):
        query = self.client.query(kind = 'ArRecipes')
        trans_entities = list(map(from_datastore,query.fetch()))
        return trans_entities

    def insert(self,title,author,ingredientslist,preperationtime,skilllevel,description):
        key = self.client.key('Recipe')
        recipe = datastore.Entity(key)
        recipe.update( {
            'title': title,
            'author' : author,
            'ingred_list' : ingredientslist,
            'prep_time' : preperationtime,
            'skill_lv' : skilllevel,
            'descrip' : description
            })
        self.client.put(recipe)
        return True

    def insert_translated(self,title,authoer,ingredientslist,preperationtime,skilllevel,description):
        key = self.cleint.key('ArRecipes')
        recipes_translated = datastore.Entity(key)
        recipe_translated.update( {
            'title': title,
            'author' : author,
            'ingred_list' : ingredientslist,
            'prep_time' : preperationtime,
            'skill_lv' : skilllevel,
            'descrip' : description
            })
        self.client.put(recipe_translated)
        return True

