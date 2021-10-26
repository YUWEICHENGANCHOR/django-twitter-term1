from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        # 關注者1關注了你(recipient)
        # actor = User1
        # verb = 'followed'
        # user1 給你發的帖子tweet1點了讚
        # actor = user1
        # target = tweet1
        # verb = 給你發的帖子點了讚
        model = Notification
        fields = (
            'id',
            'actor_content_type',
            'actor_object_id',
            'verb',
            'action_object_content_type',
            'action_object_object_id',
            'target_content_type',
            'target_object_id',
            'timestamp',
            'unread',
        )