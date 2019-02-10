这篇文章比较有启发性的是从另外一个角度来思考

作者提出


– Engineers are not good at repairing
– Engineers make mistakes taking things apart... (undoing...?) 
– Engineers made mistakes putting things back together...(redoing...?) 

从这里就可以延伸出去想到工程师可能会犯错的地方

- Explicit Pairings
    – Direct: 'on/off', 'true/false', properties.
    - e.g. 

        + ``display="block"/"none"``
        + ``appendChild/removeChild``
        + addEventListener : ``focusin/focusout``
- Implicit Pairings
    - Indirect: inheritance, nullity, state change.
    - e.g.

        + Content: ``innerText=''/ document.write('')``
        + Relation: swap parent/child node
        + Status: ``window.navigate('') / location.reload()``
- Hybrid Pairings
    - Complexity of mixing explicit and implicit.
    - Script (Dynamic) + HTML (Static)

        + ``<body contentEditable='true'>``
        + ``Document.body.contentEditable='false';``
    - Property + Method
- Pairing Combinations
    – Multiple pairings per page.
