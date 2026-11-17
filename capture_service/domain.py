"""解释领域原文；待核来源不转换成确认结论。"""
import json
def decode(raw,receipt):
    d=json.loads(raw.decode('utf-8'))
    if d.get('revision')!='r1':raise ValueError('来源版次不明')
    identity=str(d.get('hour'))
    if not identity or identity=='None':raise ValueError('来源身份不明')
    typ='hour'
    if d.get('utc_offset')=='-05:00':typ='support'
    return [{'type':typ,'id':identity,'version':d['revision'],'payload':d}]
def assess(rows):
    primary=[r for r in rows if r['type']=='hour']
    support=[r for r in rows if r['type']=='support']
    reasons=['重复本地小时与跨区交换仍待对齐']
    if not primary:reasons.append('缺少主要来源')
    if not support:reasons.append('缺少关联来源')
    return {'publishable':False,'reasons':reasons,'primary_count':len(primary),'support_count':len(support)}
