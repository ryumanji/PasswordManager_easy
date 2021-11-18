【導入】
1. pythonを入れる
2. モジュールをインストール（下記コマンドを実施）
pip install -r requirements.txt

3. pathを通す
※システム環境変数が操作できない場合は、管理者権限を付けたPowerShellにて下記コマンドを実行
Start C:\Windows\system32\rundll32.exe sysdm.cpl, EditEnvironmentVariables

【使用方法】
windowsキー + R を押し、pw.pyw <サービス> <項目> を入力
例) pw.pyw redmine PASS

pass_list.ymlの書き方

<サービス>:
  <項目>: "データ" 

注意) データに " を使用する場合は ' で囲む


