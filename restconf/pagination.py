from rest_framework import pagination

class CFEAPIPagination(pagination.PageNumberPagination):
    page_size = 5
    
    # default_limit = 6
    # max_limit = 20
    
    # limit_query_param = 'lim'