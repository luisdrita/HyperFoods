# Recipe1M Dataset

## Layers

### layer1.json

```js
{
  id: String,  // unique 10-digit hex string
  title: String,
  instructions: [ { text: String } ],
  ingredients: [ { text: String } ],
  partition: ('train'|'test'|'val'),
  url: String
}
```

### layer2.json

```js
{
  id: String,   // refers to an id in layer 1
  images: [ {
    id: String, // unique 10-digit hex + .jpg
    url: String
  } ]
}
```

## Images

The images in each of the partitions, train/val/test, are arranged in a four-level hierarchy corresponding to the first four digits of the image id.

For example: `val/e/f/3/d/ef3dc0de11.jpg`

The images are in RGB JPEG format and can be loaded using standard libraries.
