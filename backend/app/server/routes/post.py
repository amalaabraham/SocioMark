from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..controllers.post import (
    add_post,
    delete_post,
    retrieve_post,
    update_post,
    report_post
)
from ..models.post import (
    ResponseModel,
    PostSchema,
    UpdatePostModel,
)

router = APIRouter()


@router.post("/create", response_description="Post added into the database")
async def add_post_data(post: PostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = await add_post(post)
    return ResponseModel(new_post, "Post created successfully.")


@router.delete("/delete", response_description="Delete post from the database")
async def delete_post_data(post_id: str):
    new_post = await delete_post(post_id)
    return ResponseModel(new_post, "Post deleted successfully.")


@router.patch("/update", response_description="Update post")
async def update_post_data(post_id: str, updated_post: UpdatePostModel = Body(...)):
    updated_post = jsonable_encoder(updated_post)
    new_post = await update_post(post_id, updated_post)
    return ResponseModel(new_post, "Post updated successfully.")


@router.post("/report", response_description="Report post")
async def report_post_data(post_id: str):
    new_post = await report_post(post_id)
    return ResponseModel(new_post, "Post reported successfully.")


@router.get("/details", response_description="Get post details from the database")
async def details_post_data(post_id: str):
    new_post = await retrieve_post(post_id)
    return ResponseModel(new_post, "Got post details successfully.")