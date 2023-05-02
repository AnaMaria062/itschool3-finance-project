from fastapi import APIRouter, Depends, HTTPException, status

from domain.asset.factory import AssetFactory
from domain.asset.repo import AssetRepo
from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo, AssetInfoUser, AssetAdd
from persistence.user_file import UserPersistenceFile
from persistence.user_sqlite import UserPersistenceSqlite

users_router = APIRouter(prefix="/users")


def get_user_repo() -> UserRepo:
    # user_persistence = UserPersistenceFile("main_users.json")
    user_persistence = UserPersistenceSqlite()
    return UserRepo(user_persistence)


@users_router.get("", response_model=list[UserInfo])
def get_all_users(repo=Depends(get_user_repo)):
    return repo.get_all()


@users_router.get("/{user_id}", response_model=UserInfo)
def get_user(user_id: str, repo=Depends(get_user_repo)):
    return repo.get_by_id(user_id)


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd, repo=Depends(get_user_repo)):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user


@users_router.delete("/{user_id}")
def delete_user(user_id: str, repo=Depends(get_user_repo)):
    if repo.delete(user_id):
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}


# TODO fix api, return asset info


@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, asset: AssetAdd, repo=Depends(get_user_repo)):
    try:
        new_asset = AssetFactory().make_new(asset.ticker)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid asset ticker provided",
        )

    user = repo.get_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    AssetRepo().add_to_user(user, new_asset)
    asset_info = AssetInfoUser(user_id=user_id, asset=new_asset)
    return asset_info
