# pydicom tools

pydicomを用いてDICOM RTを解析するときのツール群です。

## 3次元CTデータの構築

以下の方法で変数`ct`に3次元Volumeを読み込みます。

```python
from pydicom_tools import CTImage
ct = CTImage()
ct.load(path_to_ct)
```

## DRRの生成

以下の方法でDRRを生成します。
DRRの作成にはITKが必要です。事前にpipなどでインストールしてください。

```console
pip install itk
```

```python
from pydicom_tools import DRR
drr = DRR(ct, beam, size)
```

`ct`は`CTImage`クラスのインスタンス、`beam`はBeamSequenceのオブジェクト、
`size`はDRRのmm単位のサイズです。


## RT Structure Setの読み込み

以下の方法でRT Structure Setを読み込みます。

```python
from pydicom_toos import RTSS
ss = RTSS('path/to/rtss')

# 輪郭名一覧を表示
print(ss.structures)

# z座標をkeyとする輪郭点座標の辞書へアクセス
points = ss.points['Structure Name']

# z座標をkeyとするmatplotlib.path.Pathクラスのオブジェクトへアクセス
paths = ss.paths['Structure Name']

# 輪郭の体積を計算
volume = ss.calc_volume('Structure Name')
```