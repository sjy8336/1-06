# 회원가입 프로젝트 - dict / list 활용
# - 회원가입 / 전체 회원목록 / 로그인 / 종료
users = []  # 전체 회원목록을 가질 예정
# 회원 1명 정보는 dict에 저장
# u1 = {name: '김회원', userId : 'Kim', passwd: '123'}
data = {}
keys = ('name', 'userId', 'passwd')
# CLI 프로그램 - command Line Interface  터미널에서 실행되는 프로그램
# GUI 프로그램 - Graphic User Interface  그래픽 화면을 갖춘 프로그램
while True:
    print('------------------------------------------------')
    print('1. 회원가입 2. 회원목록 3. 로그인 9. 종료')
    print('------------------------------------------------')
    menu = int(input('메뉴 번호를 선택하세요 >>'))
    # print(menu)
    # 메뉴에 없는 번호를 입력할 경우
    # 입력 오류!! 메뉴번호를 입력해야 출력 후 다시 입력받기
    # 1 선택 => 이름 / 아이디 / 비번 입력받아 data에 저장 후 users에 data저장
    # 2 선택 => 전체 회원 정보 출력 (이름과 아이디만)
    # 3 선택 => 아이디 / 비번 입력받기
    #           해당 회원이 맞으면 "환영합니다" / 틀리면 "아이디 또는 비밀번호가 일치하지 않습니다"
    # 9 선택 => 시스템 종료 break / exit() 함수
    if menu == 9:
        print('Bye Bye!')
        # break
        exit(0)  # 시스템 종료
        # 유효성 체크
    if menu < 1 or menu > 3:
        print('입력 오류!! 메뉴에 없는 번호입니다.')
        continue
    if menu == 1:
        name = input('이름 입력:')
        userId = input('아이디 입력:')
        passwd = input('비밀번호 입력:')
        data = {keys[0]: name, keys[1]: userId, keys[2]: passwd}
        users.append(data)
        print('회원 가입 완료!! 현재 회원수:', len(users),'명')
    elif menu == 2:
        print(f'번호 : Name\tUser ID')
        print('-'*30)
        for idx, user in enumerate(users):
            print(f'{idx + 1}: {user.get(keys[0])}\t{user[keys[1]]}')
    elif menu == 3:
        uid = input('ID 입력: ')
        upw = input('PW 입력: ')
        isLogin = False
        for user in users:
            if uid == user['userId']:   # 아이디가 회원이 맞다면
                if upw == user['passwd']:
                    isLogin = True
                    break
                else:
                    isLogin = False
                    # 비밀번호 일치하지 않는 경우
                    print('아이디 또는 비밀번호가 일치하지 않습니다')
                    continue
        if isLogin:
            print(f'{user.get('name')}님 환영합니다~!!!')



""" if menu == 1:
        name = input('이름을 입력하세요 >>')
        userId = input('아이디를 입력하세요 >>')
        passwd = input('비밀번호를 입력하세요 >>')
        data = name, userId, passwd
        print(data)
        users.append(data)
        print(users)
    elif menu == 2:
        for a, b, c in users.items():
            print(f'{a}, {b}')
    elif menu == 3:
        userId2 = input('아이디를 입력하세요>>')
        passwd2 = input('비밀번호 입력하세요>>')
        """

# [문제 2] 위 코드를 리팩토링 하세요
# 함수로 모듈화하여 재구성해보기
# 회원가입 처리 함수 signup()
# 로그인 처리 함수 signin()
# 전체 회원정보 출력 printAll()
# 함수로 로직을 구성하고 메뉴번호에 따라 해당 함수를 호출하여
# 프로그램이 잘 실행되도록 개선해봅시다

