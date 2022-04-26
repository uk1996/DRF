from rest_framework import permissions

# 포스팅 작성자가 아니라면, 읽기 권한만 부여하기
class IsAuthorOrReadOnly(permissions.BasePermission):
    # APIView 접근 시 체크
    # 인증된 유저에 한해, 목록 조회/포스팅 등록을 허용
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # get_object 함수를 통해 object 획득 시에 체크
    # 작성자에 한해, Record에 대한 수정/삭제 허용
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # 조회요청(GET, HEAD, OPTIONS)에 대해서는 인증여부에 상관없이 허용
            return True
        return obj.author == request.user