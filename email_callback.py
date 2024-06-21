def email_callback(email, name):
    # 将特定的旧邮箱替换为新邮箱
    if email == 'sun_zengchang@163.com':
        return ('Ivan-Sun', '19359022+Ivan-sun@users.noreply.github.com')  # 请替换为你的公开邮箱地址
    else:
        # 对于其他邮箱保持不变
        return (name, email)

# 确保脚本可以独立运行时不会执行任何操作
if __name__ == '__main__':
    pass