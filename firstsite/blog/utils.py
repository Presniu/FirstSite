class DataMixin:

    paginate_by = 3

    def get_post_content(self, **kwargs):
        content = kwargs
        return content
