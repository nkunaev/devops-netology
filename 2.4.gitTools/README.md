1. Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea?
aefead2207ef7e2aa5dc81a34aedf0cad4c32545  Update CHANGELOG.md

UDP
git show aefea
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>

2. Какому тегу соответствует коммит 85024d3?
v0.12.23

UDP
PS C:\my_projects\devops-netology\terra_full> git show 85024d3
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)
Author: tf-release-bot <terraform@hashicorp.com>
Date:   Thu Mar 5 20:56:10 2020 +0000

    v0.12.23 <- tag

3. Сколько родителей у коммита b8d720? Напишите их хеши.

*   b8d720f834 Merge pull request #23916 from hashicorp/cgriggs01-stable
|\
| * 9ea88f22fc add/update community provider listings - 1й 
|/
*   56cd7859e0 Merge pull request #23857 from hashicorp/cgriggs01-stable 2-й 

UDP
PS C:\my_projects\devops-netology\terra_full> git log b8d720 -3 --graph --oneline
*   b8d720f834 Merge pull request #23916 from hashicorp/cgriggs01-stable 
|\
| * 9ea88f22fc add/update community provider listings
|/
*   56cd7859e0 Merge pull request #23857 from hashicorp/cgriggs01-stable

4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.

PS C:\my_projects\devops-netology\terra_full> git log --oneline v0.12.23..v0.12.24 
33ff1c03bb (tag: v0.12.24) v0.12.24
b14b74c493 [Website] vmc provider links
3f235065b9 Update CHANGELOG.md
6ae64e247b registry: Fix panic when server is unreachable
5c619ca1ba website: Remove links to the getting started guide's old location
06275647e2 Update CHANGELOG.md
d5f9411f51 command: Fix bug when using terraform login on Windows
4b6d06cc5d Update CHANGELOG.md
dd01a35078 Update CHANGELOG.md
225466bc3e Cleanup after v0.12.23 release
(END)

5. Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так 
func providerSource(...) (вместо троеточия перечислены аргументы). 
git log -L :providerSource:provider_source.go --oneline

8c928e8358 main: Consult local directories as potential mirrors of providers

diff --git a/provider_source.go b/provider_source.go
--- /dev/null
+++ b/provider_source.go
@@ -0,0 +19,5 @@
+func providerSource(services *disco.Disco) getproviders.Source {
+       // We're not yet using the CLI config here because we've not implemented
+       // yet the new configuration constructs to customize provider search
+       // locations. That'll come later.
+       // For now, we have a fixed set of search directories:

6. Найдите все коммиты в которых была изменена функция globalPluginDirs.
Сначала нашел упоминание о функции git grep -n globalPluginDirs и файле, в котором она была. Потом по 
файлу смотрел историю через log -L

78b1220558 Remove config.go and update things using its aliases
-       dir, err := ConfigDir()
+       dir, err := cliconfig.ConfigDir()
52dbf94834
+               ret = append(ret, filepath.Join(dir, "plugins"))
                ret = append(ret, filepath.Join(dir, "plugins", machineDir))
41ab0aef7a
-               ret = append(ret, filepath.Join(dir, "plugins"))
+               machineDir := fmt.Sprintf("%s_%s", runtime.GOOS, runtime.GOARCH)
+               ret = append(ret, filepath.Join(dir, "plugins", machineDir))
66ebff90cd
-
-       // Look in the same directory as the Terraform executable.
-       // If found, this replaces what we found in the config path.
-       exePath, err := osext.Executable()
-       if err != nil {
-               log.Printf("[ERROR] Error discovering exe directory: %s", err)
8364383c35
+func globalPluginDirs() []string {
+       var ret []string
+
+       // Look in the same directory as the Terraform executable.
+       // If found, this replaces what we found in the config path.
+       exePath, err := osext.Executable()
+       if err != nil {
+               log.Printf("[ERROR] Error discovering exe directory: %s", err)
+       } else {
+               ret = append(ret, filepath.Dir(exePath))

7. Кто автор функции synchronizedWriters?
git log -S synchronizedWriters  

main: synchronize writes to VT100-faker on Windows

Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Wed May 3 16:25:41 2017 -0700
