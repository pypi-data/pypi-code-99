from enum import IntEnum
from typing import Optional, TYPE_CHECKING, Union, Dict, Any, List

import attr
from aiohttp import FormData

from dis_snek.const import MISSING
from dis_snek.mixins.send import SendMixin
from dis_snek.models.discord import DiscordObject
from dis_snek.models.snowflake import to_snowflake
from dis_snek.utils.attr_utils import define
from dis_snek.utils.input_utils import _bytes_to_base64_data

if TYPE_CHECKING:
    from io import IOBase
    from pathlib import Path

    from dis_snek.client import Snake
    from dis_snek.models.snowflake import Snowflake_Type
    from dis_snek.models.discord_objects.channel import TYPE_MESSAGEABLE_CHANNEL
    from dis_snek.models.discord_objects.components import BaseComponent
    from dis_snek.models.discord_objects.embed import Embed
    from dis_snek.models.discord_objects.message import AllowedMentions, Message, MessageReference
    from dis_snek.models.discord_objects.sticker import Sticker


class WebhookTypes(IntEnum):
    INCOMING = 1
    """Incoming Webhooks can post messages to channels with a generated token"""
    CHANNEL_FOLLOWER = 2
    """Channel Follower Webhooks are internal webhooks used with Channel Following to post new messages into channels"""
    APPLICATION = 3
    """Application webhooks are webhooks used with Interactions"""


@define
class Webhook(DiscordObject, SendMixin):
    type: WebhookTypes = attr.ib()
    """The type of webhook"""

    application_id: Optional["Snowflake_Type"] = attr.ib(default=None)
    """the bot/OAuth2 application that created this webhook"""

    guild_id: Optional["Snowflake_Type"] = attr.ib(default=None)
    """the guild id this webhook is for, if any"""
    channel_id: Optional["Snowflake_Type"] = attr.ib(default=None)
    """the channel id this webhook is for, if any"""
    user_id: Optional["Snowflake_Type"] = attr.ib(default=None)
    """the user this webhook was created by"""

    name: Optional[str] = attr.ib(default=None)
    """the default name of the webhook"""
    avatar: Optional[str] = attr.ib(default=None)
    """the default user avatar hash of the webhook"""
    token: str = attr.ib()
    """the secure token of the webhook (returned for Incoming Webhooks)"""
    url: Optional[str] = attr.ib(default=None)
    """the url used for executing the webhook (returned by the webhooks OAuth2 flow)"""

    source_guild_id: Optional["Snowflake_Type"] = attr.ib(default=None)
    """the guild of the channel that this webhook is following (returned for Channel Follower Webhooks)"""
    source_channel_id: Optional["Snowflake_Type"] = attr.ib(default=None)
    """the channel that this webhook is following (returned for Channel Follower Webhooks)"""

    @classmethod
    async def create(
        cls,
        client: "Snake",
        channel: Union["Snowflake_Type", "TYPE_MESSAGEABLE_CHANNEL"],
        name: str,
        avatar: Optional[bytes] = MISSING,
    ):
        """
        Create a webhook.

        parameters:
            client: The bot's client
            channel: The channel to create the webhook in
            name: The name of the webhook
            avatar: An optional default avatar to use
        """
        if name.lower() == "clyde":
            raise ValueError('Webhook names cannot be "Clyde"')

        if not isinstance(channel, (str, int)):
            channel = to_snowflake(channel)

        if avatar:
            avatar = _bytes_to_base64_data(avatar)

        data = await client.http.create_webhook(channel, name, avatar)

        new_cls = cls.from_dict(data, client)

        return new_cls

    @classmethod
    def _process_dict(cls, data: Dict[str, Any], client: "Snake") -> Dict[str, Any]:
        if data.get("user"):
            user = client.cache.place_user_data(data.pop("user"))
            data["user_id"] = user.id
        return data

    async def delete(self) -> None:
        """Delete this webhook"""
        await self._client.http.delete_webhook(self.id, self.token)

    async def _send_http_request(self, message_payload: Union[dict, "FormData"]) -> dict:
        return await self._client.http.execute_webhook(self.id, self.token, message_payload)

    async def send(
        self,
        content: Optional[str] = None,
        embeds: Optional[Union[List[Union["Embed", dict]], Union["Embed", dict]]] = None,
        components: Optional[
            Union[List[List[Union["BaseComponent", dict]]], List[Union["BaseComponent", dict]], "BaseComponent", dict]
        ] = None,
        stickers: Optional[Union[List[Union["Sticker", "Snowflake_Type"]], "Sticker", "Snowflake_Type"]] = None,
        allowed_mentions: Optional[Union["AllowedMentions", dict]] = None,
        reply_to: Optional[Union["MessageReference", "Message", dict, "Snowflake_Type"]] = None,
        file: Optional[Union["IOBase", "Path", str]] = None,
        tts: bool = False,
        flags: Optional[Union[int, "MessageFlags"]] = None,
        username: str = None,
        avatar_url: str = None,
    ):
        """
        Send a message as this webhook

        parameters:
            content: Message text content.
            embeds: Embedded rich content (up to 6000 characters).
            components: The components to include with the message.
            stickers: IDs of up to 3 stickers in the server to send in the message.
            allowed_mentions: Allowed mentions for the message.
            reply_to: Message to reference, must be from the same channel.
            filepath: Location of file to send, defaults to None.
            tts: Should this message use Text To Speech.
            flags: Message flags to apply.
            username: The username to use
            avatar_url: The url of an image to use as the avatar

        returns:
            New message object that was sent.
        """
        return await super().send(
            content,
            embeds,
            components,
            stickers,
            allowed_mentions,
            reply_to,
            file,
            tts,
            flags,
            username=username,
            avatar_url=avatar_url,
        )

    # todo: edit webhook messaage
