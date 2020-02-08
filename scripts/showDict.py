# Actionable commands which are passed into a function for further processing
# Python character limit ignored due to performance concerns with powershell

show_command_set = {
	'show arp':'arp -a',
	'show bgp advert':'Get-BgpRouteAggregate',
	'show bgp id':'Get-BgpRouter | Select-Object BgpIdentifier, LocalASN, TransitRouting, RouteReflector | Format-List',
	'show bgp peer':'Get-BgpPeer -Verbose | Format-List',
	'show crypto':'Get-VpnConnection | Select-Object -Property Name, ServerAddress,TunnelType,AuthenticationMethod, ConnectionStatus',
	'show dns cache':'Get-DnsClientCache | Sort-Object -Property Entry | Format-Table -AutoSize',
	'show dns server':'Get-DnsClientServerAddress | Sort-Object -Property AddressFamily | Format-Table -Autosize',
	'show drives':'Get-Volume',
	'show fwall profile':'Get-NetFirewallProfile',
	'show gpo':'gpresult /R',
	'show int':'get-netadapter | Sort-Object -Property Status -Descending | Format-Table -AutoSize',
	'show ip address':'Get-NetIPAddress -AddressFamily IPv4 | Select-Object -Property ifIndex,InterfaceAlias,IPAddress,PrefixLength,PrefixOrigin | Sort-Object -Property IPAddress | Format-Table -AutoSize',
	'show ip public':'(Invoke-WebRequest https://itomation.ca/mypublicip).content',
	'show ip route':'Get-NetRoute -AddressFamily ipv4 | Sort-Object -Property DestinationPrefix | Format-Table -Autosize',
	'show ipv6 address':'Get-NetIPAddress -AddressFamily IPv6 | Select-Object -Property ifIndex,InterfaceAlias,IPAddress,PrefixLength,PrefixOrigin | Sort-Object -Property IPAddress | Format-Table -AutoSize',
	'show ipv6 public':'(Invoke-WebRequest ip6only.me/api/).content',
	'show ipv6 route':'Get-NetRoute -AddressFamily ipv6 | Sort-Object -Property DestinationPrefix | Format-Table -Autosize',
	'show log wev':'eventvwr.msc',
	'show powershell version':'$PSVersionTable | Format-Table -HideTableHeaders',
	'show proc top':'Get-Process | Sort-Object -Property WS | Select-Object -Last 10 | sort-object -Property CPU -Descending',
	'show proc':'Get-Process | Sort-Object -Property CPU -Descending',
	'show programs':r'Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table -AutoSize',
	'show svc':'Get-Service | Sort-Object -Property Status -Descending | Format-Table -AutoSize',
	'show tcp':'netstat -n',
}