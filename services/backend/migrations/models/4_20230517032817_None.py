from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "project" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "project_name" VARCHAR(256) NOT NULL,
    "district" VARCHAR(5) NOT NULL,
    "version" VARCHAR(8) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "ankerwowis" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "list_index" INT NOT NULL,
    "source" VARCHAR(17) NOT NULL,
    "kne" VARCHAR(256) NOT NULL,
    "coverage" DOUBLE PRECISION NOT NULL,
    "project_id" INT NOT NULL REFERENCES "project" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "ankerwowis"."source" IS 'OBJECT_LIST: Object List\nUNIVERSAL_DATASET: Universal Dataset';
CREATE TABLE IF NOT EXISTS "costs" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "ap_usage" DOUBLE PRECISION NOT NULL,
    "separator" VARCHAR(1) NOT NULL,
    "activation_ngn" BOOL NOT NULL,
    "ngn_cost_jump_to_ngn" DOUBLE PRECISION NOT NULL,
    "ngn_cost_per_meter" DOUBLE PRECISION NOT NULL,
    "recommendation_flag_vrp" VARCHAR(18) NOT NULL,
    "project_id" INT NOT NULL REFERENCES "project" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "costs"."separator" IS 'Realistic: 1\nHigh: 2';
COMMENT ON COLUMN "costs"."recommendation_flag_vrp" IS 'RECOMMENDATION_50: recommendation_50\nRECOMMENDATION_64: recommendation_64\nRECOMMENDATION_100: recommendation_100\nRECOMMENDATION_150: recommendation_150\nRECOMMENDATION_175: recommendation_175\nRECOMMENDATION_200: recommendation_200';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
