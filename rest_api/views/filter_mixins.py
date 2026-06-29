"""Common mixins for view filtering behavior."""


class QueryParamFilterMixin:
    """Add query parameter filtering support to ModelViewSet classes."""

    allowed_filters = []

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_params = {
            key: value
            for key, value in self.request.query_params.items()
            if key in self.allowed_filters and value != ""
        }

        if filter_params:
            queryset = queryset.filter(**filter_params)

        return queryset
