import shutil
src = rwd+format_path(args[0])
dst = rwd+format_path(args[1])
shutil.copy(src, dst)