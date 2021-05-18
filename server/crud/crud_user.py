from bson.objectid import ObjectId
from server.db.database import user_collection


def user_helper(user) -> dict:
    return {
        'id': str(user["_id"]),
        'username': user["username"],
        'email': user["email"],
        'firstname': user["firstname"],
        'lastname': user["lastname"],
        'password': user["password"]
    }


async def get_all():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


async def get_by_id(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


async def create(model: dict) -> dict:
    user = await user_collection.insert_one(model)
    new_user = await user_collection.find_one({'_id': user.inserted_id})
    if new_user:
        return user_helper(new_user)


async def delete(id: str) -> bool:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update(id: str, update_model: dict) -> bool:
    if len(update_model) < 1:
        return False

    user = await user_collection.find_one({'_id': ObjectId(id)})
    if user:
        update_user = user_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "firstname": update_model.get('firstname'),
                "lastname": update_model.get('lastname'),
                "password": update_model.get('password'),
                "avatar": update_model.get('avatar')
            }}
        )
        if update_user:
            return True
    return False
