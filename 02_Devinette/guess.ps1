param (
	[int]$min	= 0,
	[int]$max	= 1000
)

[int]$answer	= Get-Random -Minimum $min -Maximum $max

[bool]$HasGuessed	= $false

$InputPromptGuess		= "Tentative #"
$InputPromptUserName	= "Veuillez entrer votre nom d'utilisateur"
$GameplayFail			= "Echec: "
$GameplayPromptLower	= "${GameplayFail}Trop bas."
$GameplayPromptHigher	= "${GameplayFail}Trop élevé."

$ErrorMsg	= "Erreur: "
$TryAgain	= "Veuillez réessayer."
$ErrorMin	= "${ErrorMsg}Nombre trop petit: ${TryAgain}"
$ErrorMax	= "${ErrorMsg}Nombre trop élevé: ${TryAgain}"

$player	= Read-Host -Prompt "${InputPromptUserName}"

[int]$tries = 1
while ( $HasGuessed -eq $false ) {
	[int]$guess = Read-Host -Prompt "${InputPromptGuess}${tries}"
	if ( $guess -lt $min) {
		Write-Host $ErrorMin;
		continue
	}
	elseif ( $guess -gt $max ) {
		Write-Host $ErrorMax;
		continue
	}
	if ( $guess -ne $answer ) {
		$tries++
		if ( $guess -lt $answer ) {
			Write-Host $GameplayPromptLower
		} elseif ( $guess -gt $answer ) {
			Write-Host $GameplayPromptHigher
		}
	} else {
		$HasGuessed = $true
		Write-Host	"Félicitation ${player}: Vous avez trouvé la réponse"`
					"en ${tries} essais!"
	}
}
