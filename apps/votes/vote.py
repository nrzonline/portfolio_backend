from votes.models import Vote, VOTE_CHOICES


def cast_vote(vote, ip_address, content_type, object_id):
    Vote.objects.create(
        vote=vote,
        ip_address=ip_address,
        content_type=content_type,
        object_id=object_id
    )


def get_object_vote_count(vote_value, content_type, object_id):
    return Vote.objects.filter(
        vote=vote_value,
        content_type=content_type,
        object_id=object_id
    ).count()


def get_object_vote_value_for_ip_address(ip_address, content_type, object_id):
    try:
        vote_cast = Vote.objects.get(
            ip_address=ip_address,
            content_type=content_type,
            object_id=object_id,
        )
        return vote_cast.vote
    except Vote.DoesNotExist:
        return None


def is_vote_valid_option(vote):
    return vote in dict(VOTE_CHOICES)
