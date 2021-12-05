from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password: str):
        return password_context.hash(password)

    def verify(src_hashed_password: str, target_password: str):
        return password_context.verify(target_password, src_hashed_password)
