f = File.new("teste_ruby.txt", "w")
n = 999999
ini = Time.now
s = n ** n
fim = Time.now

f.write(ini.to_s + ' ' + ((ini.to_f - ini.to_i) * 1000).to_s + "ms\n")
f.write(fim.to_s + ' ' + ((fim.to_f - fim.to_i) * 1000).to_s + "ms\n")
f.write(s)
f.close

