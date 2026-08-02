from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.services.auth_service import get_current_user


def require_role(*roles: str):
    def checker(
        current_user: User = Depends(get_current_user),
    ):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )

        return current_user

    return checker
