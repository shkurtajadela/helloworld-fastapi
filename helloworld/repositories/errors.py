class RepositoryError(Exception):
    pass


class NotFoundError(RepositoryError):
    pass


class UniqueViolationError(RepositoryError):
    pass


class ForeignKeyViolationError(RepositoryError):
    pass
