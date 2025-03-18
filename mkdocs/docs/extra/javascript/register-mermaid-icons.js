import mermaid from 'https://unpkg.com/mermaid@11.4.0/dist/mermaid.esm.min.mjs'
document$.subscribe(function() {
  console.log("Initialize third-party libraries here")
  mermaid.registerIconPacks([
    // logos
    {
      name: 'logos',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/logos@1/icons.json').then((res) => res.json()),
    },
    //skill-icons
    {
      name: 'skill-icons',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/skill-icons@1/icons.json').then((res) => res.json()),
    },
    //heroicons
    {
      name: 'heroicons',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/heroicons@1/icons.json').then((res) => res.json()),
    },
    //carbon
    {
      name: 'carbon',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/carbon@1/icons.json').then((res) => res.json()),
    },
    //material-symbols
    {
      name: 'material-symbols',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/material-symbols@1/icons.json').then((res) => res.json()),
    },
    //codicon
    {
      name: 'codicon',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/codicon@1/icons.json').then((res) => res.json()),
    },
    //solar
    {
      name: 'solar',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/solar@1/icons.json').then((res) => res.json()),
    },
    //simple-icons
    {
      name: 'simple-icons',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/simple-icons@1/icons.json').then((res) => res.json()),
    },
    //hugeicons
    {
      name: 'hugeicons',
      loader: () =>
        fetch('https://unpkg.com/@iconify-json/hugeicons@1/icons.json').then((res) => res.json()),
    },
  ])
  mermaid.run({querySelector: '.diagram'});
});