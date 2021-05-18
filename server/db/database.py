import motor.motor_asyncio

MONGO_DETAILS = "mongodb://sa:0nhopass@cluster0-shard-00-00.9trco.mongodb.net:27017," \
                "cluster0-shard-00-01.9trco.mongodb.net:27017," \
                "cluster0-shard-00-02.9trco.mongodb.net:27017/waof?ssl=true&replicaSet=atlas-mrtir6-shard-0" \
                "&authSource=admin&retryWrites=true"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.waof

test_db = client.test

user_collection = database.get_collection('users_collection')
product_collection = database.get_collection('products_collection')
