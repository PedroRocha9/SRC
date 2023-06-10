# Let's analise only the data_normal

# get the mean between all src_ip:
#   - flows 
#   - flows to internet
#   - flows to private ips
#   - flows to servers
#   - total up_bytes
#   - up_bytes_per_flow
#   - total down_bytes
#   - down_bytes_per_flow
#   - % of udp flows
#   - % of tcp flows
data_normal = 'data_normal.parquet'

normal_stat = data_normal.groupby(['src_ip']).size().reset_index(name='flows')
normal_stat['flows_to_internet'] = data_normal.loc[(data_normal['dst_ip'].apply(lambda x: ipaddress.ip_address(x).is_private)==False)].groupby(['src_ip']).size().reset_index(name='flows_to_internet')['flows_to_internet']
normal_stat['flows_to_private_ips'] = data_normal.loc[(data_normal['dst_ip'].apply(lambda x: ipaddress.ip_address(x).is_private))].groupby(['src_ip']).size().reset_index(name='flows_to_private_ips')['flows_to_private_ips']
normal_stat['total_up_bytes'] = data_normal.groupby(['src_ip'])['up_bytes'].sum().reset_index(name='up_bytes')['up_bytes']
normal_stat['up_bytes_per_flow'] = data_normal.groupby(['src_ip'])['up_bytes'].sum().reset_index(name='up_bytes')['up_bytes']/normal_stat['flows']
normal_stat['total_down_bytes'] = data_normal.groupby(['src_ip'])['down_bytes'].sum().reset_index(name='down_bytes')['down_bytes']
normal_stat['down_bytes_per_flow'] = data_normal.groupby(['src_ip'])['down_bytes'].sum().reset_index(name='down_bytes')['down_bytes']/normal_stat['flows']
normal_stat['% udp_flows'] = data_normal.loc[(data_normal['proto']=='udp')].groupby(['src_ip']).size().reset_index(name='udp_flows')['udp_flows']/normal_stat['flows']
normal_stat['% tcp_flows'] = data_normal.loc[(data_normal['proto']=='tcp')].groupby(['src_ip']).size().reset_index(name='tcp_flows')['tcp_flows']/normal_stat['flows']

mean_flows = normal_stat['flows'].mean()
mean_flows_to_internet = normal_stat['flows_to_internet'].mean()
mean_flows_to_private_ips = normal_stat['flows_to_private_ips'].mean()
mean_total_up_bytes = normal_stat['total_up_bytes'].mean()
mean_up_bytes_per_flow = normal_stat['up_bytes_per_flow'].mean()
mean_total_down_bytes = normal_stat['total_down_bytes'].mean()
mean_down_bytes_per_flow = normal_stat['down_bytes_per_flow'].mean()
mean_perc_udp_flows = normal_stat['% udp_flows'].mean()
mean_perc_tcp_flows = normal_stat['% tcp_flows'].mean()



# stats for country
# - flows to country
# - up_bytes to country
# - down_bytes to country
# - up_bytes per flow to country
# - down_bytes per flow to country
normal_country_stat = data_normal.loc[(data_normal['dst_ip'].apply(lambda x: not ipaddress.ip_address(x).is_private))].groupby(['dst_country']).size().reset_index(name='flows_to_country')
normal_country_stat['up_bytes_to_country'] = data_normal.loc[(data_normal['dst_ip'].apply(lambda x: not ipaddress.ip_address(x).is_private))].groupby(['dst_country'])['up_bytes'].sum().reset_index(name='up_bytes')['up_bytes']
normal_country_stat['down_bytes_to_country'] = data_normal.loc[(data_normal['dst_ip'].apply(lambda x: not ipaddress.ip_address(x).is_private))].groupby(['dst_country'])['down_bytes'].sum().reset_index(name='down_bytes')['down_bytes']
normal_country_stat['up_bytes_per_flow_to_country'] = normal_country_stat['up_bytes_to_country']/normal_country_stat['flows_to_country']
normal_country_stat['down_bytes_per_flow_to_country'] = normal_country_stat['down_bytes_to_country']/normal_country_stat['flows_to_country']

mean_flows_to_country = normal_country_stat['flows_to_country'].mean()
mean_up_bytes_to_country = normal_country_stat['up_bytes_to_country'].mean()
mean_down_bytes_to_country = normal_country_stat['down_bytes_to_country'].mean()
mean_up_bytes_per_flow_to_country = normal_country_stat['up_bytes_per_flow_to_country'].mean()
mean_down_bytes_per_flow_to_country = normal_country_stat['down_bytes_per_flow_to_country'].mean()