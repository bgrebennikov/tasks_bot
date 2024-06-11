from api.abs.ApiClientAbs import ApiClientAbs
from api.data.responseDto.UserDto import UserDto


class ApiClient(ApiClientAbs):
    user: UserDto = None

    def __init__(self):
        super().__init__()

    def initProfile(self, user: UserDto):
        upsert = self.user is not None
        self.user = user
        return user

    def getProfile(self, profile_id: int):
        self.user.first_join = True
        return self.user
