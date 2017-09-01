from votes.models import Vote, VOTE_CHOICES


def get_object_vote_cast_by_ip_address(ip_address, content_type, object_id):
    vote_cast = Vote.objects.filter(
        ip_address=ip_address,
        content_type=content_type,
        object_id=object_id,
    )
    if vote_cast:
        return vote_cast.last()
    return None


def is_vote_valid_option(vote):
    return vote in dict(VOTE_CHOICES)
