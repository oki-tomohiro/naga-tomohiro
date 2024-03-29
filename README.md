# naga-tomohiro

始めに,リポジトリを作成する時,自分の名前が推測されるようなリポジトリ名にしてしまった.
リポジトリ名を変えようと試みたが,どうやらリンクの更新等様々な手順が必要となることがわかり,
時間の都合上このままのリポジトリ名にさせていだたきたいと思う.
今後は,個人情報が推測されないようなリポジトリ名にすることを心がける.

作成したコードはheartrate.pyにある.
カメラから動画を取得して表示するコードは,https://weblabo.oscasierra.net/python/opencv-videocapture-camera.html
の"カメラから動画を取得して表示するサンプル"より引用した.この引用は,heartrate.pyの5,11,16,17,18,22,23,25,26行目にある.
また,FPS表示のコードは,https://note.nkmk.me/python-opencv-fps-measure/
の,"FPSの取得"より引用した.この引用は,heartrate.pyの36,38行目にある.

上の引用に加えて,私は新たに,12-14,19-21,28,29,31-34行目を実装した.14行目で
1次元の配列imを1000000だけ作る.
このimは毎フレームの輝度値の平均を格納するもので,1000000フレーム分の輝度値の平均が格納できる.
19行目で,毎フレームごとにcountを1ずつ足している.また,21行目でiに1を足すことで,配列imの添え字を操作している.
こうすることで,グラフにプロットする時に,輝度値の平均が連続的になる.
28行目で,0フレーム目からcountフレームまで,count個に分割し,
29行目で,配列imを0からcount-1までプロットしている.このように,xとyの配列の数が合うようにしている(エラーが起きない).

実行の仕方としては,実行の際,カメラの正面の映像が出てくるので,
パソコンのカメラに指をくっつけ,側に光を照らして明るくする.
この時,画面が赤くなり,明るさが脈拍に合わせて微妙に変化することが観察できるように指や光を調節する.
測り終えるときは,qを押す(カメラ画像にフォーカスされているとき).
gifを見ると,左手でカメラを指でくっつけ,スマホで光を当てている様子がわかる.
下に輝度値の平均がプロットされたグラフと,FPSが表示される.
グラフを見たとき,値が一定期間で変化しているところがある.それが脈拍である.
FPSが表示されるので,ある期間の脈拍数とFPSから心拍数を計算することができる.
今回,FPSが30なので,例えば期間が300の間の脈拍数を測った場合,これは10秒の脈拍数を測ったということなので,この数の約6倍が心拍数となる.
下のグラフを見ると,一定の期間で,輝度値の平均が変化していることがわかる.

依存ライブラリとしては,mathと,カメラ画像のためのcv2(opencv),配列arrayのためのnumpy,
グラフ描写のためのmatplotlibを利用した.

バージョンは,3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]である.

![demo](https://raw.github.com/wiki/oki-tomohiro/naga-tomohiro/images/heartrate.gif)

![demo](https://raw.github.com/wiki/oki-tomohiro/naga-tomohiro/images/heartrate1.jpg)