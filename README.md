Node and npm have to be installed

```
node -v
npm -v
```

Install kingraph

```
npm install -g rstacruz/kingraph
```

Increase max [memory](https://github.com/rstacruz/kingraph/issues/6#issuecomment-2477596647) size

Configure `family.yml` according [guide](https://github.com/rstacruz/kingraph/blob/master/docs/getting_started.md)

Use it for creating `family.html` with family tree

```
kingraph family.yml -s ALLOW_MEMORY_GROWTH=1 | Out-File -FilePath "family.html" -Encoding oem
```

> Possible Encoding: unknown,string,unicode,bigendianunicode,utf8,utf7,utf32,ascii,default,oem

Install [markdown-viewer](https://github.com/simov/markdown-viewer) for browser

Open `family.html` file in browser

Enjoy