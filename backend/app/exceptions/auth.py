class AuthError(Exception):
    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail
        super().__init__(self.detail)


class UserAlreadyExistsError(AuthError):
    def __init__(self, username: str) -> None:
        self.username = username
        self.detail = f"User '{username}' already exists"
        super().__init__(self.detail)


class EmailAlreadyExistsError(AuthError):
    def __init__(self, email: str) -> None:
        self.email = email
        self.detail = f"Email '{email}' is already registered"
        super().__init__(self.detail)


class InvalidUserCredentialsError(AuthError):
    def __init__(self) -> None:
        self.detail = "Invalid username or password"
        super().__init__(self.detail)


class InvalidTokenError(AuthError):
    def __init__(self) -> None:
        self.detail = "Invalid or expired token"
        super().__init__(self.detail)
