test_schema = {
    'collections': [
        {
            'name': 'Question', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'choice', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'Choice.id', 'inverse_of': None, 'relationship': 'HasMany', 'widget': None,
                 'validations': []},
                {'field': 'id', 'type': 'Number', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'question_text', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'pub_date', 'type': 'Date', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []}]},
        {
            'name': 'Choice', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'id', 'type': 'Number', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'question', 'type': 'Number', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': 'Question.id', 'inverse_of': None, 'relationship': 'BelongsTo',
                 'widget': None, 'validations': []},
                {'field': 'choice_text', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'votes', 'type': 'Number', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []}]},
        {
            'name': 'Session', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'session_key', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'session_data', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'expire_date', 'type': 'Date', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []}]},
        {
            'name': 'Publication', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'article', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'Article.id', 'inverse_of': None, 'relationship': 'HasMany', 'widget': None,
                 'validations': []},
                {'field': 'id', 'type': 'Number', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'title', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []}]},
        {
            'name': 'Article', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'id', 'type': 'Number', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'headline', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'publications', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': 'Publication.id', 'inverse_of': None, 'relationship': 'HasMany',
                 'widget': None, 'validations': []}]},
        {
            'name': 'Permission', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'group', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'Group.id', 'inverse_of': None, 'relationship': 'HasMany', 'widget': None,
                 'validations': []},
                {'field': 'user', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'User.id',
                 'inverse_of': None, 'relationship': 'HasMany', 'widget': None, 'validations': []},
                {'field': 'id', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'name', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'content_type', 'type': 'Number', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'ContentType.id', 'inverse_of': None, 'relationship': 'BelongsTo', 'widget': None,
                 'validations': []},
                {'field': 'codename', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []}]},
        {
            'name': 'Group', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'user', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'User.id', 'inverse_of': None, 'relationship': 'HasMany', 'widget': None,
                 'validations': []},
                {'field': 'id', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'name', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'permissions', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': 'Permission.id', 'inverse_of': None, 'relationship': 'HasMany',
                 'widget': None, 'validations': []}]},
        {
            'name': 'User', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'id', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'password', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'last_login', 'type': 'Date', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False,
                 'default_value': None, 'integration': None, 'reference': None, 'inverse_of': None,
                 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'is_superuser', 'type': 'Boolean', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'username', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False,
                 'default_value': None, 'integration': None, 'reference': None, 'inverse_of': None,
                 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'first_name', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'last_name', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'email', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'is_staff', 'type': 'Boolean', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'is_active', 'type': 'Boolean', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'date_joined', 'type': 'Date', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': None, 'inverse_of': None, 'relationship': None, 'widget': None,
                 'validations': []},
                {'field': 'groups', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False,
                 'default_value': None, 'integration': None, 'reference': 'Group.id',
                 'inverse_of': None, 'relationship': 'HasMany', 'widget': None, 'validations': []},
                {'field': 'user_permissions', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False, 'is_required': False, 'is_virtual': False, 'default_value': None,
                 'integration': None, 'reference': 'Permission.id', 'inverse_of': None, 'relationship': 'HasMany',
                 'widget': None, 'validations': []}]},
        {
            'name': 'ContentType', 'is_virtual': False, 'icon': None, 'is_read_only': False, 'is_searchable': True,
            'only_for_relationships': False, 'pagination_type': 'page', 'search_fields': None, 'actions': [],
            'segments': [],
            'fields': [
                {'field': 'permission', 'type': ['Number'], 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': 'Permission.id', 'inverse_of': None, 'relationship': 'HasMany', 'widget': None,
                 'validations': []},
                {'field': 'id', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'app_label', 'type': 'String', 'is_filterable': True, 'is_sortable': True,
                 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []},
                {'field': 'model', 'type': 'String', 'is_filterable': True, 'is_sortable': True, 'is_read_only': False,
                 'is_required': False, 'is_virtual': False, 'default_value': None, 'integration': None,
                 'reference': None,
                 'inverse_of': None, 'relationship': None, 'widget': None, 'validations': []}]}],
    'meta': {
        'database_type': 'sqlite',
        'liana': 'django-forest',
        'liana_version': '0.0.0',
        'orm_version': '9.9.9'
    }
}
