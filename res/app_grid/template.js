
function escapeString(s){
    return s.replaceAll("'","apos;").replaceAll("\\","\\\\")
}

function applyTemplate( _template, obj, escapeValue = false ){
	var result = _template
    
    Object.keys(obj).forEach( (key) => {
    	result = replaceAll(result, key, escapeValue? escapeString(obj[key])   : obj[key])
    } )
    
    return result
}

function replaceAll(sTarget, sToReplace, sWith ){
	console.log("sWith: \'" + sWith + "\'")
    return sTarget.replace(
    	new RegExp( "\{\{"+sToReplace+"\}\}", "g"), 
        sWith
    )
}