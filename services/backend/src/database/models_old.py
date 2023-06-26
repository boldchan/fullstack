from enum import Enum, unique
from tortoise import fields, models

@unique
class WoWiSource(Enum):
    OBJECT_LIST = 'Object List'
    UNIVERSAL_DATASET = 'Universal Dataset' 

@unique
class RecommendationFlagVRP(Enum):
    RECOMMENDATION_50 = 'recommendation_50'
    RECOMMENDATION_64 = 'recommendation_64'
    RECOMMENDATION_100 = 'recommendation_100'
    RECOMMENDATION_150 = 'recommendation_150'
    RECOMMENDATION_175 = 'recommendation_175'
    RECOMMENDATION_200 = 'recommendation_200'


class Project(models.Model):
    id = fields.IntField(pk=True)
    project_name = fields.CharField(max_length=256, null=False)
    district: str = fields.CharField(max_length=5, null=False)
    version: str = fields.CharField(max_length=8, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class AnkerWoWis(models.Model):
    id = fields.IntField(pk=True)
    list_index = fields.IntField()
    project = fields.ForeignKeyField("models.Project", related_name='anker_wowi')
    source = fields.CharEnumField(WoWiSource)
    kne = fields.CharField(max_length=256, null=False)
    coverage = fields.FloatField()


class Costs(models.Model):
    id = fields.IntField(pk=True)
    ap_usage = fields.FloatField()
    separator = fields.CharEnumField(Enum('SeparatorCost', ['Realistic', 'High']))
    activation_ngn = fields.BooleanField()
    ngn_cost_jump_to_ngn = fields.FloatField()
    ngn_cost_per_meter = fields.FloatField()
    recommendation_flag_vrp = fields.CharEnumField(RecommendationFlagVRP)
    project = fields.ForeignKeyField("models.Project", related_name='costs')

