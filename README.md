Node and npm have to be installed

```
node -v
npm -v
```

Install kingraph

```
npm install -g rstacruz/kingraph
```

Configure `family.yml` according [guide](https://github.com/rstacruz/kingraph/blob/master/docs/getting_started.md)

Use it for creating family.html with family tree

```
kingraph family.yml | Out-File -FilePath "family.html" -Encoding oem
```

> Possible Encoding: unknown,string,unicode,bigendianunicode,utf8,utf7,utf32,ascii,default,oem

Open `family.html` file in browser
