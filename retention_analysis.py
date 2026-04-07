def calculate_retention_metrics(data):
    # Initialize metrics
    metrics = {
        '保单上传率': 0,
        '续保线索分配率': 0,
        '续保线索跟进率': 0,
        '续保线索成功率': 0,
        '事故发生率': 0,
        '事故预估产值': 0,
        '续保ROI': 0,
        '产保比': 0
    }

    # Data quality checks
    if not data:  # Check if data is empty
        print("数据为空，无法进行计算。")
        return metrics
    
    # Perform calculations
    try:
        total_policies_uploaded = sum(entry['uploaded'] for entry in data)
        total_renewal_leads = sum(entry['renewal_leads'] for entry in data)
        total_followed_leads = sum(entry['followed_leads'] for entry in data)
        total_successful_leads = sum(entry['successful_leads'] for entry in data)
        total_incidents = sum(entry['incidents'] for entry in data)
        total_estimated_value = sum(entry['estimated_value'] for entry in data)
        total_renewal_cost = sum(entry['renewal_cost'] for entry in data)
        
        # Calculate metrics
        metrics['保单上传率'] = total_policies_uploaded / len(data) if data else 0
        metrics['续保线索分配率'] = total_renewal_leads / total_policies_uploaded if total_policies_uploaded else 0
        metrics['续保线索跟进率'] = total_followed_leads / total_renewal_leads if total_renewal_leads else 0
        metrics['续保线索成功率'] = total_successful_leads / total_followed_leads if total_followed_leads else 0
        metrics['事故发生率'] = total_incidents / len(data) if data else 0
        metrics['事故预估产值'] = total_estimated_value / total_incidents if total_incidents else 0
        metrics['续保ROI'] = (total_estimated_value - total_renewal_cost) / total_renewal_cost if total_renewal_cost else 0
        metrics['产保比'] = total_estimated_value / total_renewal_cost if total_renewal_cost else 0
    except Exception as e:
        print(f'计算过程中出现错误: {e}')

    return metrics

# Example usage:
# data = [
#     {'uploaded': 1, 'renewal_leads': 5, 'followed_leads': 4, 'successful_leads': 3, 'incidents': 1, 'estimated_value': 2000, 'renewal_cost': 500},
#     {'uploaded': 1, 'renewal_leads': 3, 'followed_leads': 2, 'successful_leads': 1, 'incidents': 0, 'estimated_value': 1500, 'renewal_cost': 300}
# ]
# metrics = calculate_retention_metrics(data)
# print(metrics)